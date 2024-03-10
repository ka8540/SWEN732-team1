import React, { useState } from 'react';
import { View, Text, FlatList, StyleSheet, TouchableOpacity } from 'react-native';

// Static data for shopping cart items (In a real app, this could come from an API or device storage)
const SHOPPING_CART_ITEMS = [
  { id: '1', title: 'Product Item 1', quantity: 1 },
  { id: '2', title: 'Product Item 2', quantity: 2 },
  { id: '3', title: 'Product Item 3', quantity: 3 },
  // Add more items as needed
];

const ShoppingCart = () => {
  // State to manage cart items
  const [cartItems, setCartItems] = useState(SHOPPING_CART_ITEMS);

  // Render each item in the list
  const renderItem = ({ item }) => (
    <View style={styles.itemContainer}>
      <Text style={styles.itemText}>{item.title}</Text>
      <Text style={styles.quantityText}>Quantity: {item.quantity}</Text>
    </View>
  );

  return (
    <View style={styles.container}>
      <Text style={styles.title}>My Shopping Cart</Text>
      <FlatList
        data={cartItems}
        renderItem={renderItem}
        keyExtractor={item => item.id}
      />
    </View>
  );
};

// Styles for the shopping cart screen components
const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    paddingTop: 20,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  itemContainer: {
    backgroundColor: '#f9c2ff',
    padding: 20,
    marginVertical: 8,
    marginHorizontal: 16,
    borderRadius: 5,
    flexDirection: 'row',
    justifyContent: 'space-between', // To separate the title and quantity
  },
  itemText: {
    fontSize: 18,
  },
  quantityText: {
    fontSize: 16,
    fontWeight: 'bold',
  },
});

// Export the ShoppingCart component to use it in your app
export default ShoppingCart;
