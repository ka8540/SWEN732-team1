import React, { useState } from 'react';
import PropTypes from 'prop-types'; // Import PropTypes
import { SafeAreaView, View, Text, StyleSheet } from 'react-native';

const FAVOURITE_ITEMS = [
  { id: '1', title: 'Favourite Item 1' },
  { id: '2', title: 'Favourite Item 2' },
  { id: '3', title: 'Favourite Item 3' },
];

const FavouritesScreen = ({ navigation }) => {
  const [favourites, setFavourites] = useState(FAVOURITE_ITEMS);

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

FavouritesScreen.propTypes = {
  navigation: PropTypes.object.isRequired, // Define the prop type for navigation
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  content: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
});

export default FavouritesScreen;
