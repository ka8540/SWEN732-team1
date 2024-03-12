import React, { useState } from 'react';
import { Ionicons } from '@expo/vector-icons';
import { SafeAreaView, View, Text, StyleSheet, TouchableOpacity } from 'react-native';

const FAVOURITE_ITEMS = [
  { id: '1', title: 'Favourite Item 1' },
  { id: '2', title: 'Favourite Item 2' },
  { id: '3', title: 'Favourite Item 3' },
];

const FavouritesScreen = ({ navigation }) => {
  const [favourites, setFavourites] = useState(FAVOURITE_ITEMS);

  // Now, these functions are defined inside the component, so they have access to the `navigation` prop.

  const renderItem = ({ item }) => (
    <View style={styles.itemContainer}>
      <Text style={styles.itemText}>{item.title}</Text>
    </View>
  );

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.content}>
        <Text>FAVOURITE_ITEMS</Text>
      </View>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  navbar: {
    height: 60,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: 'cyan',
  },
  navbarText: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#fff',
  },
  content: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  footer: {
    flexDirection: 'row',
    height: 60,
    alignItems: 'center',
    justifyContent: 'space-around',
    backgroundColor: 'cyan',
  },
  footerButton: {
    paddingHorizontal: 10,
    paddingVertical: 10,
  },
});

export default FavouritesScreen;
