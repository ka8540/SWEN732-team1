import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, Image, ScrollView, Button, ActivityIndicator, TouchableOpacity, TextInput } from 'react-native';
import { useRoute } from '@react-navigation/native';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { Picker } from '@react-native-picker/picker';
import { ActionSheetIOS } from 'react-native';
const ProductDetails = () => {
  const [productDescription, setProductDescription] = useState('');
  const [product, setProduct] = useState(null);
  const [retailers, setRetailers] = useState([]);
  const [priceInfo, setPriceInfo] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedCurrency, setSelectedCurrency] = useState('USD');
  const [convertedPrice, setConvertedPrice] = useState('');
  const [quantity, setQuantity] = useState('1'); // Default quantity
  const route = useRoute();
  const { ProductID } = route.params;
  
  const showCurrencyOptions = () => {
    const options = ['USD', 'CAD', 'INR', 'Cancel'];
    const cancelButtonIndex = options.length - 1;
    
    ActionSheetIOS.showActionSheetWithOptions(
      {
        options: options,
        cancelButtonIndex: cancelButtonIndex,
        userInterfaceStyle: 'light' // This should make it have the silver background
      },
      (buttonIndex) => {
        if (buttonIndex !== cancelButtonIndex) {
          setSelectedCurrency(options[buttonIndex]);
        }
      }
    );
  };
  
  useEffect(() => {
    const fetchProductDetails = async () => {

      try {
        const productResponse = await fetch(`http://127.0.0.1:5000/products/${ProductID}`);
        const productData = await productResponse.json();
        setProduct(productData);

        if (productData && productData.ProductDescription) {
          const formattedDescription = productData.ProductDescription.split('\\n').join('\n\n');
          setProductDescription(formattedDescription);
        }

        const retailersResponse = await fetch('http://127.0.0.1:5000/retailers');
        const retailersData = await retailersResponse.json();
        setRetailers(retailersData);

        const priceResponse = await fetch('http://127.0.0.1:5000/prices');
        const priceData = await priceResponse.json();
        const productPriceInfo = priceData.find(price => price.ProductID === ProductID);
        setPriceInfo(productPriceInfo);
        
      } catch (e) {
        setError('Failed to fetch data: ' + e.toString());
      } finally {
        setLoading(false);
      }
    };

    fetchProductDetails();
  }, [ProductID]);

  useEffect(() => {
    const fetchConvertedPrice = async () => {
      if (selectedCurrency === 'USD' || !priceInfo.Price) return;
  
      const endpoint = selectedCurrency === 'CAD' ? '/cad_price' : '/inr_price';
      const url = `http://127.0.0.1:5000${endpoint}`;
      try {
        const response = await fetch(url, {
          method: 'GET',
          headers: { 'Price': priceInfo.Price.toString() },
        });
        if (!response.ok) throw new Error('Price conversion failed');
        const result = await response.json();
  
        // Check the selected currency and set the state accordingly
        if (selectedCurrency === 'CAD') {
          setConvertedPrice(result.price_cad);
        } else if (selectedCurrency === 'INR') {
          setConvertedPrice(result.price_inr);
        }
        
        console.log(result); // This will log the correct value
      } catch (error) {
        setError(`Failed to convert price: ${error.message}`);
      }
    };
  
    fetchConvertedPrice();
  }, [priceInfo, selectedCurrency]);
  
  const handleAddToFavorites = async () => {
    const sessionKey = await AsyncStorage.getItem('sessionKey');
    if (!sessionKey) {
      console.error('Session key not found. User might not be logged in.');
      return;
    }

    const response = await fetch('http://127.0.0.1:5000/user_favorites', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-Session-Key': sessionKey,
      },
      body: JSON.stringify({ product_id: ProductID }),
    });

    if (!response.ok) {
      console.error('Problem adding product to favorites');
    } else {
      console.log('Product added to favorites');
    }
  };

  const handleAddToCart = async () => {
    const sessionKey = await AsyncStorage.getItem('sessionKey');
    if (!sessionKey) {
      console.error('Session key not found. User might not be logged in.');
      return;
    }

    const response = await fetch('http://127.0.0.1:5000/cart', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-Session-Key': sessionKey,
      },
      body: JSON.stringify({ product_id: ProductID, quantity: parseInt(quantity, 10) }),
    });

    if (!response.ok) {
      console.error('Problem adding product to cart');
    } else {
      console.log('Product added to cart');
    }
  };

  if (loading) {
    return <View style={styles.centered}><ActivityIndicator size="large" /></View>;
  }

  if (error) {
    return <View style={styles.centered}><Text>{error}</Text></View>;
  }

  return (
    <ScrollView contentContainerStyle={styles.container}>
      {product && (
        <>
          <Text style={styles.productTitle}>{product.ProductName}</Text>
          <Image source={{ uri: product.ImageURL }} style={styles.productImage} />
          <TextInput
            style={styles.quantityInput}
            value={quantity}
            onChangeText={setQuantity}
            keyboardType="numeric"
            placeholder="Quantity"
          />
          
          <TouchableOpacity
            onPress={handleAddToFavorites}
            style={styles.buttonFavorite}
          >
            <Text style={styles.buttonText}>Add to Favorite</Text>
          </TouchableOpacity>

          <TouchableOpacity
            onPress={handleAddToCart}
            style={styles.buttonCart}
          >
            <Text style={styles.buttonText}>Add to Cart</Text>
          </TouchableOpacity>
          
          <View style={{ flexDirection: 'row', justifyContent: 'center', alignItems: 'center', marginVertical: 10 }}>
            <TouchableOpacity
              onPress={showCurrencyOptions}
              style={styles.currencyButton}
            >
              <Text style={styles.buttonText}>Choose Currency</Text>
            </TouchableOpacity>
          </View>
          <Text style={styles.productDescription}>{productDescription}</Text>
          {retailers.map((retailer) => (
              <View key={retailer.RetailerID} style={styles.retailerContainer}>
                <Text style={styles.retailerName}>{retailer.RetailerName}</Text>
                <Text style={styles.productPrice}>
                  {selectedCurrency === 'USD' ? priceInfo.Price : convertedPrice}
                </Text>
              </View>
            ))}


        </>
      )}
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flexGrow: 1,
    justifyContent: 'flex-start', // Aligns content to the top of the screen
    alignItems: 'center',
    backgroundColor: '#f0f0f0', // Soft background color
    padding: 20,
  },
  productTitle: {
    fontSize: 28, // Larger font size for product title
    fontWeight: 'bold',
    color: '#333', // Darker color for better readability
    marginTop: 20,
    textAlign: 'center', // Center-align the text
  },
  productImage: {
    width: '100%',
    height: 250, // Adjusted for proportionate display
    resizeMode: 'contain',
    borderRadius: 10, // Rounded corners for the image
    marginTop: 20,
  },
  quantityInput: {
    fontSize: 18,
    height: 50, // Taller touch area
    width: '80%', // Consistent width with the buttons
    borderColor: '#ccc',
    borderWidth: 1,
    borderRadius: 5, // Rounded corners for the input field
    padding: 10,
    backgroundColor: '#fff', // White background to stand out from container
    marginBottom: 20,
    marginTop:20,
  },
  buttonFavorite: {
    backgroundColor: '#ff4444', // Red for the favorite button
    paddingVertical: 15, // Slightly more padding for a larger button
    width: '90%', // Set a consistent width
    borderRadius: 10, // Rounded corners
    alignSelf: 'center', // Center the button
    marginTop: 10, // Space from the top element
    marginBottom: 5, // Space from the bottom element
    elevation: 2, // Drop shadow for Android (optional)
    shadowColor: '#000', // Black color for the shadow
    shadowOffset: { width: 0, height: 2 }, // Positioning of the shadow
    shadowOpacity: 0.25, // Opacity of the shadow
    shadowRadius: 3.84,
    marginBottom: 10,
  },
  buttonCart: {
    backgroundColor: '#008000', // Green for the cart button
    paddingVertical: 15, // Slightly more padding for a larger button
    width: '90%', // Set a consistent width
    borderRadius: 10, // Rounded corners
    alignSelf: 'center', // Center the button
    marginTop: 5, // Space from the top element
    marginBottom: 10, // Space from the bottom element
    elevation: 2, // Drop shadow for Android (optional)
    shadowColor: '#000', // Black color for the shadow
    shadowOffset: { width: 0, height: 2 }, // Positioning of the shadow
    shadowOpacity: 0.25, // Opacity of the shadow
    shadowRadius: 3.84, // Blur radius of the shadow
    marginBottom: 15,
  },
  buttonText: {
    color: '#ffffff', // White text color
    fontSize: 18, // Slightly larger font size
    fontWeight: '600', // Medium font weight
    textAlign: 'center', // Center text
    fontSize: 20,
  },
  productDescription: {
    fontSize: 18,
    color: '#666', // Dark grey for readability
    textAlign: 'justify', // Justified text for cleaner presentation
    marginBottom: 20,
    paddingHorizontal: 10, // Padding to prevent text from touching screen edges
  },
  retailerContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: 10,
    borderBottomWidth: 1,
    borderBottomColor: '#E0E0E0',
    width: '100%',
    marginBottom: 10,
  },
  retailerName: {
    fontSize: 20,
    fontWeight: '600',
    color: '#007bff', // Slightly darker for better visibility
  },
  priceContainer: { // Create a new style for the price container
    flexDirection: 'row',
    justifyContent: 'flex-end',
    alignItems: 'center',
  },
  productPrice: {
    fontSize: 18,
    fontWeight: '600', // Bold for the price
    color: '#008000', // Green for the price
    marginLeft: 4, // Space between the retailer name and the price
  },
  pickerContainer: {
    borderColor: '#ccc',
    borderWidth: 1,
    borderRadius: 5,
    width: '80%', // Consistent width with other elements
    marginBottom: 20,
    backgroundColor: '#fff',
  },
  currencyButton: {
    backgroundColor: '#dcdcdc', // Silver background color
    paddingHorizontal: 20,
    paddingVertical: 10,
    borderRadius: 5,
    marginHorizontal: 5,
    elevation: 2, // Optional for Android shadow
    shadowColor: '#000', // Optional for iOS shadow
    shadowOffset: { width: 0, height: 1 },
    shadowOpacity: 0.22,
    shadowRadius: 2.22,
  },
});

export default ProductDetails;
