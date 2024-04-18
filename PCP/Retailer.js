import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, Image, ScrollView, Button, ActivityIndicator, TouchableOpacity } from 'react-native';
import { useRoute } from '@react-navigation/native';
import AsyncStorage from '@react-native-async-storage/async-storage';
const ProductDetails = () => {
  const [productDescription, setProductDescription] = useState('');
  const [product, setProduct] = useState(null);
  const [retailers, setRetailers] = useState([]);
  const [priceInfo, setPriceInfo] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const route = useRoute();
  const { ProductID } = route.params; 
  const [userId, setUserId] = useState(null);
  
  useEffect(() => {
    const fetchProductDetails = async () => {
      try {
        // Fetch product details
        const productResponse = await fetch(`http://127.0.0.1:5000/products/${ProductID}`);
        const productData = await productResponse.json();
        setProduct(productData);
        
        if (productData && productData.ProductDescription) {
          // Split the description into paragraphs and rejoin with double newlines
          const formattedDescription = productData.ProductDescription.split('\\n').join('\n\n\n\n');
          setProductDescription(formattedDescription);
        }

        // Fetch retailers
        const retailersResponse = await fetch('http://127.0.0.1:5000/retailers');
        const retailersData = await retailersResponse.json();
        setRetailers(retailersData);
        
        // Fetch price information
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

  if (loading) {
    return <View style={styles.centered}><ActivityIndicator size="large" /></View>;
  }

  if (error) {
    return <View style={styles.centered}><Text>{error}</Text></View>;
  }

  const handleAddToFavorites = async () => {
    try {
      // Retrieve the session key from storage
      const sessionKey = await AsyncStorage.getItem('sessionKey');
      console.log("Session Key:",sessionKey);
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
        body: JSON.stringify({
          product_id: ProductID, 
        }),
      });
      console.log("ProductId:",ProductID);

      if (!response.ok) {
        throw new Error('Problem adding product to favorites');
      }

      const result = await response.json();
      console.log('Product added to favorites:', result);
      // Provide feedback to the user here, such as updating the UI or showing a message
    } catch (error) {
      console.error("Error adding product to favorites:", error);
      // Provide error feedback to the user here
    }
  };

  return (
    <ScrollView contentContainerStyle={styles.container}>
      {product && (
        <>
          <Text style={styles.productTitle}>{product.ProductName}</Text>
          <Image source={{ uri: product.ImageURL }} style={styles.productImage} />
          {/* Add to Favorite Button */}
          <Button
            title="Add to Favorite"
            onPress={handleAddToFavorites}
            color="#ff4444" // Optional: customize the button color
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
  }
});

export default ProductDetails;