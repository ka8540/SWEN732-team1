import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, FlatList, Image } from 'react-native';
import { TouchableOpacity } from 'react-native';
import { useNavigation } from '@react-navigation/native';

const Phones = ({ route }) => {
  const { CategoryId } = route.params;
  const [phones, setPhones] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const navigation = useNavigation();
  useEffect(() => {
    const fetchProductsAndPrices = async () => {
      try {
        // Fetch all products
        const productsResponse = await fetch('http://127.0.0.1:5000/products');
        const products = await productsResponse.json();
        
        // Filter products based on CategoryId
        const filteredProducts = products.filter(product => product.CategoryID === CategoryId);
        
        // Fetch all prices
        const pricesResponse = await fetch('http://127.0.0.1:5000/prices');
        const prices = await pricesResponse.json();

        // Merge product information with price information
        const mergedData = filteredProducts.map(product => {
          const productPriceInfo = prices.find(price => price.ProductID === product.ProductID);
          return {
            ...product,
            Price: productPriceInfo ? productPriceInfo.Price : 'N/A', // Assuming there is a Price key in your prices data
            Currency: productPriceInfo ? productPriceInfo.Currency : 'USD', // Assuming Currency is specified in your prices data
          };
        });

        setPhones(mergedData);
      } catch (e) {
        setError(e.toString());
      } finally {
        setLoading(false);
      }
    };

    fetchProductsAndPrices();
  }, [CategoryId]);

  if (error) {
    return <View style={styles.centered}><Text>Error: {error}</Text></View>;
  }

  if (loading) {
    return <View style={styles.centered}><Text>Loading...</Text></View>;
  }

  const renderItem = ({ item }) => (
    <TouchableOpacity onPress={() => navigation.navigate('Retailer', { CategoryId: item.CategoryID, ProductID:item.ProductID })}>
      <View style={styles.productContainer}>
        <Image source={{ uri: item.ImageURL }} style={styles.productImage} />
        <View style={styles.infoContainer}>
          <Text style={styles.productName}>{item.ProductName}</Text>
          <Text style={styles.productPrice}>{item.Currency} {item.Price}</Text>
        </View>
      </View>
    </TouchableOpacity>
  );
  

  return (
    <FlatList
      data={phones}
      renderItem={renderItem}
      keyExtractor={item => item.ProductID.toString()}
      style={styles.list}
    />
  );
};

const styles = StyleSheet.create({
  centered: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  list: {
    backgroundColor: '#F5F5F5',
  },
  productContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    padding: 10,
    borderBottomWidth: 1,
    borderBottomColor: '#E0E0E0',
  },
  productImage: {
    width: 100,
    height: 100,
    borderRadius: 5,
  },
  infoContainer: {
    flex: 1,
    paddingHorizontal: 10,
  },
  productName: {
    fontSize: 16,
    fontWeight: 'bold',
  },
  productPrice: {
    fontSize: 16,
    color: 'green',
  },
});

export default Phones;
