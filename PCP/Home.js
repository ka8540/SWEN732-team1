import React, { useState, useEffect } from 'react';
import { Ionicons } from '@expo/vector-icons';
import { SafeAreaView, View, Text, StyleSheet, TouchableOpacity, Image, TextInput, FlatList, Dimensions } from 'react-native';
import Carousel from 'react-native-snap-carousel';
import { Button } from 'react-native';
const screenWidth = Dimensions.get('window').width;
export default function Home({navigation}) {
  const [activeIndex, setActiveIndex] = useState(0);
  const [searchQuery, setSearchQuery] = useState('');
  const [categories, setCategories] = useState([]);
  const [searchResults, setSearchResults] = useState([]);
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
    let imageSource = require('images/1M.jpeg');
    
    if (item.CategoryName === 'TV & Video') {
      imageSource = require('images/1M.jpeg');
    } else if (item.CategoryName === 'Home Audio & Theater') {
      imageSource = require('/Users/kayahir/Desktop/SWEN732-team1/images/2M.jpeg');
    } else if (item.CategoryName === 'Camera Photo & Video') {
      imageSource = require('/Users/kayahir/Desktop/SWEN732-team1/images/3M.jpeg');
    } else if (item.CategoryName === 'Cell Phones & Accessories') {
      imageSource = require('/Users/kayahir/Desktop/SWEN732-team1/images/4M.jpeg');
    } else if (item.CategoryName === 'Headphones') {
      imageSource = require('/Users/kayahir/Desktop/SWEN732-team1/images/5M.jpeg');
    } else if (item.CategoryName === 'Video Games') {
      imageSource = require('/Users/kayahir/Desktop/SWEN732-team1/images/6M.png');
    } else if (item.CategoryName === 'Bluetooth & Wireless Speakers') {
      imageSource = require('/Users/kayahir/Desktop/SWEN732-team1/images/7M.webp');
    } else if (item.CategoryName === 'Car Electronics') {
      imageSource = require('/Users/kayahir/Desktop/SWEN732-team1/images/8M.jpeg');
    } else if (item.CategoryName === 'Musical Instruments') {
      imageSource = require('/Users/kayahir/Desktop/SWEN732-team1/images/9M.png');
    } else if (item.CategoryName === 'Wearable Technology') {
      imageSource = require('/Users/kayahir/Desktop/SWEN732-team1/images/10M.jpeg');
    } else if (item.CategoryName === 'Laptops') {
      imageSource = require('/Users/kayahir/Desktop/SWEN732-team1/images/11M.jpeg');
    }
  
    return (
      <View style={styles.categoryCard}>
        <TouchableOpacity
          style={styles.button}
          onPress={() => navigation.navigate('Phones', { CategoryId: item.CategoryID })}
        >
          <Image style={styles.categoryImage} source={imageSource} />
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

  const handleSearch = async (query) => {
    try {
      const encodedQuery = encodeURIComponent(query);
      const categoryResponse = await fetch(`http://127.0.0.1:5000/categories/search?query=${encodedQuery}`);
      const categoryResults = await categoryResponse.json();

      if (categoryResults.length > 0) {
        const firstCategory = categoryResults[0];
        navigation.navigate('Phones', { CategoryId: firstCategory.CategoryID }); 
      } else {
        const productResponse = await fetch(`http://127.0.0.1:5000/products/search?query=${encodedQuery}`);
        const productResults = await productResponse.json();

        if (productResults.length > 0) {
          const firstProduct = productResults[0];
          navigation.navigate('Retailer', { ProductID: firstProduct.ProductID });
        } else {
          console.log('No categories or products found for this search query.');
        }
      }
    } catch (error) {
      console.error("Error during search:", error);
    }
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
        onChangeText={setSearchQuery} // Update to change searchQuery state
      />
      <Button
        title="Search"
        onPress={() => handleSearch(searchQuery)}
      />
    </View>

      {/* Carousel */}
      <View style={styles.carouselContainer}>
        <Carousel
          layout={"default"}
          data={carouselItems}
          sliderWidth={Dimensions.get('window').width}
          itemWidth={500}
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
        columnWrapperStyle={styles.columnWrapper}
        contentContainerStyle={styles.listContentContainer} 
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
    paddingHorizontal: 5, 
  },
  columnWrapper: {
    justifyContent: 'space-between', 
  },
  listContentContainer: {
    paddingHorizontal: -12000, 
  },
  button: {
    justifyContent: 'center', 
    alignItems: 'center',
    margin: 5, 
    backgroundColor: 'white',
    paddingVertical: 20,
    borderRadius: 5,
    height: 170,
    width: (screenWidth / 2) - 12,
  },
  buttonText: {
    color: '#000', 
    fontSize: 16, 
  },
  categoryImage: {
    width: '90%',
    height: '100%', 
    resizeMode: 'contain', 
    marginBottom: 5,
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
    height: 250, 
    flex: 0.5,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: 'white',
    overflow: 'hidden',
    borderRadius: 20, 
  },
  carouselItem: {
    backgroundColor: '#fff',
    borderRadius: 20, 
    width: '100%', 
    height: '100%',
    justifyContent: 'center',
    alignItems: 'center'
  },
  image: {
    width: '90%', 
    height: '100%', 
    borderRadius: 20,
    resizeMode: 'cover', 
  },
});