import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, Image, ScrollView, Button, ActivityIndicator, TouchableOpacity, TextInput } from 'react-native';
import { useRoute } from '@react-navigation/native';
import AsyncStorage from '@react-native-async-storage/async-storage';

const ProductDetails = () => {
  const [productDescription, setProductDescription] = useState('');
  const [product, setProduct] = useState(null);
  const [retailers, setRetailers] = useState([]);
  const [priceInfo, setPriceInfo] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [quantity, setQuantity] = useState('1'); // Default quantity
  const route = useRoute();
  const { ProductID } = route.params;

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
          <Button
            title="Add to Favorite"
            onPress={handleAddToFavorites}
            color="#ff4444"
          />
          <Button
            title="Add to Cart"
            onPress={handleAddToCart}
            color="#008000"
          />
          <Text style={styles.productDescription}>{productDescription}</Text>
          {retailers.map(retailer => (
            <View key={retailer.RetailerID} style={styles.retailerContainer}>
              <TouchableOpacity onPress={() => {/* navigation logic to retailer */}}>
                <Text style={styles.retailerName}>{retailer.RetailerName}</Text>
                {priceInfo && <Text style={styles.productPrice}>{priceInfo.Currency} {priceInfo.Price}</Text>}
              </TouchableOpacity>
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
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  centered: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  productTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  productImage: {
    width: '100%',
    height: 300,
    resizeMode: 'contain',
    marginBottom: 20,
  },
  productDescription: {
    fontSize: 18,
    marginBottom: 20,
  },
  productPrice: {
    fontSize: 15,
    color: 'green',
    marginBottom: 20,
  },
  retailerContainer: {
    padding: 10,
    borderBottomWidth: 1,
    borderBottomColor: '#E0E0E0',
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    width: '100%'
  },
  retailerName: {
    fontSize: 22,
    color: '#007bff'
  },
  quantityInput: {
    fontSize: 18,
    height: 40,
    width: '50%',
    borderColor: '#ccc',
    borderWidth: 1,
    padding: 10,
    marginBottom: 10
  }
});

export default ProductDetails;
