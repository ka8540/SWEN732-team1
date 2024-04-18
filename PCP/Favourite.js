import React, { useState, useEffect, useCallback } from 'react';
import {
  Image,
  SafeAreaView,
  View,
  Text,
  StyleSheet,
  FlatList,
  TouchableOpacity,
  ActivityIndicator,
  RefreshControl,
  Button,
} from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';

const FavouritesScreen = ({ navigation }) => {
  const [favourites, setFavourites] = useState([]);
  const [selectedFav, setSelectedFav] = useState(null);
  const [isLoading, setLoading] = useState(true);
  const [isRefreshing, setRefreshing] = useState(false);

  const fetchFavourites = useCallback(async () => {
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

      const favResponse = await fetch('http://127.0.0.1:5000/user_favorites', {
        headers: {
          'Content-Type': 'application/json',
          'X-Session-Key': sessionKey,
        },
      });

      if (!favResponse.ok) {
        throw new Error('Failed to fetch favourites');
      }

      let favData = await favResponse.json();
      // Filter duplicates based on ProductID
      favData = favData.filter(
        (fav, index, self) =>
          index === self.findIndex((t) => t.ProductID === fav.ProductID)
      );

      // Fetch detailed product information for each favourite
      const detailedFavourites = await Promise.all(
        favData.map(async (fav) => {
          const productResponse = await fetch(`http://127.0.0.1:5000/products/${fav.ProductID}`);
          if (!productResponse.ok) {
            throw new Error(`Failed to fetch product details for product ID ${fav.ProductID}`);
          }
          return productResponse.json();
        })
      );

      setFavourites(detailedFavourites);
    } catch (error) {
      console.error('Failed to fetch favourite items:', error);
    } finally {
      setLoading(false);
      setRefreshing(false);
    }
  }, []);

  useEffect(() => {
    fetchFavourites();
  }, [fetchFavourites]);
  
  const onRemoveFavourite = async () => {
    try {
      const sessionKey = await AsyncStorage.getItem('sessionKey');
      if (!sessionKey) {
        console.error('Session key not found');
        return;
      }
  
      const url = `http://127.0.0.1:5000/user_favorites/${selectedFav}`; // URL with the product ID
      const requestOptions = {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
          'X-Session-Key': sessionKey,
        },
      };
  
      const response = await fetch(url, requestOptions);
  
      if (response.ok) {
        // If the delete operation was successful
        console.log('Favourite deleted successfully');
        fetchFavourites(); // Refresh favourites
      } else {
        const errorText = await response.text();
        console.error('Failed to delete favourite item:', errorText);
      }
    } catch (error) {
      console.error('Failed to delete favourite item:', error);
    }
  };
  
  const onSelectFav = (productId) => {
    setSelectedFav(productId === selectedFav ? null : productId); // Toggle selection
  };

  const renderItem = ({ item }) => (
    <TouchableOpacity
      style={styles.itemContainer}
      onPress={() => onSelectFav(item.ProductID)}
    >
      <Image source={{ uri: item.ImageURL }} style={styles.itemImage} />
      <Text style={styles.itemText}>
        {item.ProductName} (ID: {item.ProductID})
      </Text>
      {selectedFav === item.ProductID && (
        <Text style={styles.selectedText}>Selected</Text>
      )}
    </TouchableOpacity>
  );

  return (
    <SafeAreaView style={styles.container}>
      {isLoading ? (
        <ActivityIndicator size="large" color="#0000ff" />
      ) : (
        <>
          <FlatList
            data={favourites}
            renderItem={renderItem}
            keyExtractor={item => item.ProductID.toString()}
            contentContainerStyle={styles.content}
            refreshControl={
              <RefreshControl
                refreshing={isRefreshing}
                onRefresh={fetchFavourites}
              />
            }
            extraData={selectedFav}
          />
          <Button
            title="Remove Selected Favourite"
            onPress={onRemoveFavourite}
            disabled={!selectedFav}
          />
        </>
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
    borderRadius: 25,
  },
  itemText: {
    fontSize: 18,
    flexShrink: 1,
  },
  selectedText: {
    color: 'blue',
    fontWeight: 'bold',
  },
  content: {
    flexGrow: 1,
  },
});

export default FavouritesScreen;
