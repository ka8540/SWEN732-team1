import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, Image, ScrollView, Button, ActivityIndicator, TouchableOpacity } from 'react-native';
import { useRoute } from '@react-navigation/native';

const ProductDetails = () => {
  const [product, setProduct] = useState(null);
  const [retailers, setRetailers] = useState([]);
  const [priceInfo, setPriceInfo] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const route = useRoute();
  const { ProductID } = route.params; // Get ProductID from navigation parameters

  useEffect(() => {
    const fetchProductDetails = async () => {
      try {
        // Fetch product details
        const productResponse = await fetch(`http://127.0.0.1:5000/products/${ProductID}`);
        const productData = await productResponse.json();
        setProduct(productData);
        
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

  return (
    <ScrollView contentContainerStyle={styles.container}>
      {product && (
        <>
          <Text style={styles.productTitle}>{product.ProductName}</Text>
          <Image source={{ uri: product.ImageURL }} style={styles.productImage} />
          <Text style={styles.productDescription}>{product.ProductDescription}</Text>
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
