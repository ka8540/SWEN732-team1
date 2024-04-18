import React, { useState, useEffect } from 'react';
import { Image, SafeAreaView, View, Text, StyleSheet, FlatList, TouchableOpacity, ActivityIndicator } from 'react-native';

const FavouritesScreen = ({ navigation }) => {
  const [favourites, setFavourites] = useState([]);
  const [isLoading, setLoading] = useState(true);

  useEffect(() => {
    const fetchFavourites = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5000/products');
        const data = await response.json();
        setFavourites(data);  
      } catch (error) {
        console.error('Failed to fetch favourite items:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchFavourites();
  }, []);  // Empty dependency array means this effect runs only once after the initial render

  const renderItem = ({ item }) => (
    <View style={styles.itemContainer}>
      <Image source={{ uri: item.ImageURL }} style={styles.itemImage} />
      <Text style={styles.itemText}>{item.ProductName} (ID: {item.ProductID})</Text>
    </View>
  );

  return (
    <SafeAreaView style={styles.container}>
      {isLoading ? (
        <View style={styles.content}>
          <ActivityIndicator size="large" color="#0000ff" />
        </View>
      ) : (
        <FlatList
          data={favourites}
          renderItem={renderItem}
          keyExtractor={item => item.ProductID.toString()}
          contentContainerStyle={styles.content}
        />
      )}
    </SafeAreaView>
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
    borderRadius: 25,  // optional, for rounded images
  },
  itemText: {
    fontSize: 18,
    flexShrink: 1,  // ensures text does not push other elements out of view
  },
  content: {
    flexGrow: 1,
    justifyContent: 'center',
  },
});

export default FavouritesScreen;