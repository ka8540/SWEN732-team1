import React, { useState, useEffect } from 'react';
import { Ionicons } from '@expo/vector-icons';
import { SafeAreaView, View, Text, StyleSheet, TouchableOpacity, Image, TextInput, FlatList, Dimensions } from 'react-native';
import Carousel from 'react-native-snap-carousel';
import { Button } from 'react-native';
export default function Home({navigation}) {
  const [activeIndex, setActiveIndex] = useState(0);
  const [searchQuery, setSearchQuery] = useState('');
  const [categories, setCategories] = useState([]);
  
  useEffect(() => {
    const fetchCategoriesAndProducts = async () => {
      try {
        // Fetch categories
        const categoriesResponse = await fetch('http://127.0.0.1:5000/categories');
        const categoriesJson = await categoriesResponse.json();
  
        // Fetch products
        const productsResponse = await fetch('http://127.0.0.1:5000/products');
        const productsJson = await productsResponse.json();
  
        // Map through categories and find the first product image for each category
        const categoriesWithImages = categoriesJson.map(category => {
          const firstProduct = productsJson.find(product => product.CategoryID === category.CategoryID);
          return {
            ...category,
            ImageURL: firstProduct ? firstProduct.ImageURL : '/Users/kayahir/Desktop/SWEN732/SWEN732-team1/images/icon.png', // Replace 'default-image-url' with your placeholder image URL
          };
        });
  
        setCategories(categoriesWithImages);
      } catch (e) {
        console.error(e);
      }
    };
  
    fetchCategoriesAndProducts();
  }, []);
  
  const renderCategoryButton = ({ item }) => {
    return (
      <View style={styles.categoryCard}>
        <TouchableOpacity
          style={styles.button}
          onPress={() => navigation.navigate('Retailer', { CategoryId: item.CategoryID })}
        >
          <Image style={styles.categoryImage} source={{ uri: item.ImageURL }} />
          <Text style={styles.buttonText}>{item.CategoryName}</Text>
        </TouchableOpacity>
      </View>
    );
  };
  
  const carouselItems = [
    {
      // Example item structure
      source: '/Users/kayahir/Desktop/SWEN732/SWEN732-team1/images/mcimage.jpeg',
    },
    {
      source: '/Users/kayahir/Desktop/SWEN732/SWEN732-team1/images/ipimage.png',
    },
    {
      source: '/Users/kayahir/Desktop/SWEN732/SWEN732-team1/images/accimage.jpeg',
    },
  ];

  const handleSearch = (query) => {
    setSearchQuery(query);
  };
  const renderItem = ({item, index}) => {
    return (
      <View style={styles.carouselItem}>
        <Image style={styles.image} source={{ uri: item.source }} />
      </View>
    );
  };

  return (
    <SafeAreaView style={styles.container}>
      {/* Navbar with Search */}
      <View style={styles.navbar}>
        <TextInput
          style={styles.searchInput}
          placeholder="Search..."
          placeholderTextColor="#888"
          value={searchQuery}
          onChangeText={handleSearch}
        />
      </View>
      {/* Carousel */}
      <View style={styles.carouselContainer}>
        <Carousel
          layout={"default"}
          data={carouselItems}
          sliderWidth={Dimensions.get('window').width}
          itemWidth={300}
          renderItem={renderItem}
          onSnapToItem={index => setActiveIndex(index)}
        />
      </View>
      {/* Main Content */}
      <View style={styles.content}>
        <FlatList
          data={categories}
          renderItem={renderCategoryButton}
          keyExtractor={item => item.CategoryID.toString()}
          numColumns={2}
          // Add the key prop here, which changes when numColumns changes
          key={2} // since numColumns is 2, you can hardcode the key as 2
          // rest of your props...
        />
      </View>


    </SafeAreaView>
  );
}

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
    flexDirection: 'row', 
    paddingHorizontal: 10, 
  },
  searchInput: {
    flex: 1, 
    height: 40,
    backgroundColor: '#fff',
    borderRadius: 20,
    paddingHorizontal: 10, 
    fontSize: 16, 
    color: '#000', 
  },
  content: {
    flex: 1,
    flexDirection: 'row', // Align children in a row
    alignItems: 'center', // Center items vertically
    justifyContent: 'flex-start', // Start from the left side
    paddingLeft: 10, // Add some padding on the left
  },
  button: {
    marginRight: 10, // Add some margin to the right of the button
    backgroundColor: 'yellow', // A light grey background for the button
    paddingHorizontal: 20, // Horizontal padding
    paddingVertical: 10, // Vertical padding
    borderRadius: 5, // Rounded corners
    height: 110,
    width: 120,
  },
  buttonText: {
    color: '#000', // Text color
    fontSize: 16, // Font size
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
  footerText: {
    fontSize: 16,
    color: '#fff',
  },
  footerIcon: {
    width: 24, 
    height: 24,
  },
  carouselContainer: {
    height: 200, 
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  carouselItem: {
    backgroundColor: '#fff',
    borderRadius: 5,
    width: '100%', 
    height: 250, 
    justifyContent: 'center',
    alignItems: 'center'
  },
  image: {
    width: 300, 
    height: 240, 
    resizeMode: 'contain', 
    paddingleft:45
  },
});
