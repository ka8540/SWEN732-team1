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
  const [favouriteItems, setFavouriteItems] = useState([]);
  const [activeFavourite, setActiveFavourite] = useState(null);
  const [isFavLoading, setFavLoading] = useState(true);
  const [isFavRefreshing, setFavRefreshing] = useState(false);

  const fetchFavouriteItems = useCallback(async () => {
    setFavLoading(true);
    setFavRefreshing(true);
    try {
      const sessionKey = await AsyncStorage.getItem('sessionKey');
      if (!sessionKey) {
        console.error('Session key not found');
        setFavLoading(false);
        setFavRefreshing(false);
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
      favData = favData.filter(
        (fav, index, self) =>
          index === self.findIndex((t) => t.ProductID === fav.ProductID)
      );

      const detailedFavourites = await Promise.all(
        favData.map(async (fav) => {
          const productResponse = await fetch(`http://127.0.0.1:5000/products/${fav.ProductID}`);
          if (!productResponse.ok) {
            throw new Error(`Failed to fetch product details for product ID ${fav.ProductID}`);
          }
          return productResponse.json();
        })
      );

      setFavouriteItems(detailedFavourites);
    } catch (error) {
      console.error('Failed to fetch favourite items:', error);
    } finally {
      setFavLoading(false);
      setFavRefreshing(false);
    }
  }, []);

  useEffect(() => {
    fetchFavouriteItems();
  }, [fetchFavouriteItems]);
  
  const onRemoveFavourite = async () => {
    try {
      const sessionKey = await AsyncStorage.getItem('sessionKey');
      if (!sessionKey) {
        console.error('Session key not found');
        return;
      }
  
      const url = `http://127.0.0.1:5000/user_favorites/${activeFavourite}`;
      const requestOptions = {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
          'X-Session-Key': sessionKey,
        },
      };
  
      const response = await fetch(url, requestOptions);
  
      if (response.ok) {
        console.log('Favourite deleted successfully');
        fetchFavouriteItems();
      } else {
        const errorText = await response.text();
        console.error('Failed to delete favourite item:', errorText);
      }
    } catch (error) {
      console.error('Failed to delete favourite item:', error);
    }
  };
  
  const onSelectFav = (productId) => {
    setActiveFavourite(productId === activeFavourite ? null : productId);
  };

  const renderItem = ({ item }) => (
    <TouchableOpacity
      style={styles.itemContainer}
      onPress={() => onSelectFav(item.ProductID)}
    >
      <Image source={{ uri: item.ImageURL }} style={styles.itemImage} />
      <Text style={styles.itemText}>
        {item.ProductName}
      </Text>
      {activeFavourite === item.ProductID && (
        <Text style={styles.selectedText}>Selected</Text>
      )}
    </TouchableOpacity>
  );

  return (
    <SafeAreaView style={styles.container}>
      {isFavLoading ? (
        <ActivityIndicator size="large" color="#0000ff" />
      ) : (
        <>
          <FlatList
            data={favouriteItems}
            renderItem={renderItem}
            keyExtractor={item => item.ProductID.toString()}
            contentContainerStyle={styles.content}
            refreshControl={
              <RefreshControl
                refreshing={isFavRefreshing}
                onRefresh={fetchFavouriteItems}
              />
            }
            extraData={activeFavourite}
          />
          <Button
            title="Remove Selected Favourite"
            onPress={onRemoveFavourite}
            disabled={!activeFavourite}
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