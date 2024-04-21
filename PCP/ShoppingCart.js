import React, { useState, useEffect, useCallback } from 'react';
import {
  View,
  Text,
  FlatList,
  StyleSheet,
  Image,
  TouchableOpacity,
  ActivityIndicator,
  RefreshControl,
  Button,
  Alert,
} from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';

const ShoppingCart = () => {
  const [cartItems, setCartItems] = useState([]);
  const [selectedItem, setSelectedItem] = useState(null);
  const [isLoading, setLoading] = useState(true);
  const [isRefreshing, setRefreshing] = useState(false);

  const onUpdateQuantity = async (productId, newQuantity) => {
    try {
      const sessionKey = await AsyncStorage.getItem('sessionKey');
      if (!sessionKey) {
        console.error('Session key not found');
        return;
      }
      const requestOptions = {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          'X-Session-Key': sessionKey,
        },
        body: JSON.stringify({ quantity: newQuantity }),
      };
      const response = await fetch(`http://127.0.0.1:5000/cart/${productId}`, requestOptions);
      if (response.ok) {
        console.log('Quantity updated successfully');
        fetchCartItems();
      } else {
        const errorText = await response.text();
        console.error('Failed to update quantity:', errorText);
      }
    } catch (error) {
      console.error('Failed to update quantity:', error);
    }
  };

  const fetchCartItems = useCallback(async () => {
    setLoading(true);
    setRefreshing(true);
    try {
      const sessionKey = await AsyncStorage.getItem('sessionKey');
      if (!sessionKey) {
        console.error('Session key not found');
        setLoading(false);
        setRefreshing(false);
        return;
      }
      const response = await fetch('http://127.0.0.1:5000/cart', {
        headers: {
          'Content-Type': 'application/json',
          'X-Session-Key': sessionKey,
        },
      });
      if (!response.ok) {
        throw new Error('Failed to fetch cart items');
      }
      const cartData = await response.json();
      const detailedCartItems = await Promise.all(
        cartData.map(async (item) => {
          const productResponse = await fetch(`http://127.0.0.1:5000/products/${item.ProductID}`);
          if (!productResponse.ok) {
            throw new Error(`Failed to fetch product details for product ID ${item.ProductID}`);
          }
          const productData = await productResponse.json();
          return {
            ...item,
            ImageURL: productData.ImageURL,
            ProductName: productData.ProductName,
          };
        })
      );
      setCartItems(detailedCartItems);
    } catch (error) {
      console.error('Failed to fetch cart items:', error);
    } finally {
      setLoading(false);
      setRefreshing(false);
    }
  }, []);

  useEffect(() => {
    fetchCartItems();
  }, [fetchCartItems]);

  const onRemoveItem = async () => {
    try {
      const sessionKey = await AsyncStorage.getItem('sessionKey');
      if (!sessionKey) {
        console.error('Session key not found');
        return;
      }
      const requestOptions = {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
          'X-Session-Key': sessionKey,
        },
      };
      const response = await fetch(`http://127.0.0.1:5000/cart/${selectedItem}`, requestOptions);
      if (response.ok) {
        console.log('Item removed from cart successfully');
        fetchCartItems();
        setSelectedItem(null);
      } else {
        const errorText = await response.text();
        console.error('Failed to remove item from cart:', errorText);
      }
    } catch (error) {
      console.error('Failed to remove item from cart:', error);
    }
  };

  const onSelectItem = (productId) => {
    setSelectedItem(productId === selectedItem ? null : productId);
  };

  const showUpdateQuantityAlert = (item) => {
    Alert.prompt(
      "Update Quantity",
      "Enter the new quantity:",
      [
        {
          text: "Cancel",
          style: "cancel"
        },
        {
          text: "Update",
          onPress: (quantity) => onUpdateQuantity(item.ProductID, parseInt(quantity))
        }
      ],
      "plain-text",
      item.Quantity.toString()
    );
  };

  const renderItem = ({ item }) => (
    <TouchableOpacity
      style={styles.itemContainer}
      onPress={() => onSelectItem(item.ProductID)}
    >
      <Image source={{ uri: item.ImageURL }} style={styles.itemImage} />
      <View style={styles.itemTextContainer}>
        <Text style={styles.itemText}>
          {item.ProductName} - Quantity: {item.Quantity}
        </Text>
        {selectedItem === item.ProductID && (
          <Button
            title="Update Quantity"
            onPress={() => showUpdateQuantityAlert(item)}
          />
        )}
      </View>
    </TouchableOpacity>
  );

  return (
    <View style={styles.container}>
      {isLoading ? (
        <ActivityIndicator size="large" color="#0000ff" />
      ) : (
        <>
          <FlatList
            data={cartItems}
            renderItem={renderItem}
            keyExtractor={item => item.ProductID.toString()}
            contentContainerStyle={styles.content}
            refreshControl={
              <RefreshControl
                refreshing={isRefreshing}
                onRefresh={fetchCartItems}
              />
            }
            extraData={selectedItem}
          />
          <Button
            title="Remove Selected Item"
            onPress={onRemoveItem}
            disabled={!selectedItem}
          />
        </>
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  itemContainer: {
    padding: 20,
    borderBottomWidth: 1,
    borderBottomColor: '#cccccc',
    flexDirection: 'row',
    alignItems: 'center',
  },
  itemImage: {
    width: 50,
    height: 50,
    marginRight: 10,
    borderRadius: 25,
  },
  itemTextContainer: {
    flex: 1,
  },
  itemText: {
    fontSize: 18,
  },
  content: {
    flexGrow: 1,
  },
});

export default ShoppingCart;
