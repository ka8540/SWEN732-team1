import React, { useState, useEffect } from 'react';
import { Ionicons } from '@expo/vector-icons';
import { SafeAreaView, View, Text, StyleSheet, TouchableOpacity, Image, TextInput, FlatList, Dimensions, Button } from 'react-native';
import Carousel from 'react-native-snap-carousel';

const screenWidth = Dimensions.get('window').width;
const categoryImageUris = {
  'TV & Video': 'https://www.digitaltrends.com/wp-content/uploads/2022/12/Sony-75-inch-X95J-Series-4K-TV.jpg',
  'Home Audio & Theater': 'https://www.bhphotovideo.com/cdn-cgi/image/format=auto,fit=scale-down,width=500,quality=95/https://www.bhphotovideo.com/images/images500x500/enclave_audio_technologies_ea_1000_pro_thx_cinehome_pro_edition_5_1_1585224397_1554695.jpg',
  'Camera Photo & Video': 'https://www.dpreview.com/files/p/articles/5481327930/panasonic-s1h-prores-raw-with-atomos-ninja-v.jpeg',
  'Cell Phones & Accessories': 'https://media.wired.com/photos/5b22c5c4b878a15e9ce80d92/master/w_2240,c_limit/iphonex-TA.jpg',
  'Headphones': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0j9eu-xoKRtWZAk701ireSFxve150zD6Swg&s',
  'Video Games': 'https://a0.anyrgb.com/pngimg/596/620/analog-stick-gamepad-joystick-game-controller-game-controllers-controller-computer-hardware-video-game-electronics-monochrome-thumbnail.png',
  'Bluetooth & Wireless Speakers': 'https://i.ebayimg.com/images/g/xIcAAOSwQBpiA3y1/s-l1200.webp',
  'Car Electronics': 'https://www.shutterstock.com/image-vector/electric-car-e-plug-green-600nw-2303576823.jpg',
  'Musical Instruments': 'https://upload.wikimedia.org/wikipedia/commons/4/45/GuitareClassique5.png',
  'Wearable Technology': 'https://m.media-amazon.com/images/I/61SxKn69eRL._AC_SL1500_.jpg',
  'Laptops': 'https://static.nationalcreditdirect.com/common/images/products/BBY-6499751_sd.jpg'
};

export default function Home({ navigation }) {
  const [activeIndex, setActiveIndex] = useState(0);
  const [searchQuery, setSearchQuery] = useState('');
  const [categories, setCategories] = useState([]);
  const [searchResults, setSearchResults] = useState([]);

  useEffect(() => {
    const fetchCategoriesAndProducts = async () => {
      try {
        const categoriesResponse = await fetch('http://127.0.0.1:5000/categories');
        const categoriesJson = await categoriesResponse.json();
        const productsResponse = await fetch('http://127.0.0.1:5000/products');
        const productsJson = await productsResponse.json();

        const categoriesWithImages = categoriesJson.map(category => {
          const firstProduct = productsJson.find(product => product.CategoryID === category.CategoryID);
          return {
            ...category,
            ImageURL: firstProduct ? firstProduct.ImageURL : '/Users/kayahir/Desktop/SWEN732/SWEN732-team1/images/icon.png',
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
    const imageSource = { uri: categoryImageUris[item.CategoryName] || 'https://via.placeholder.com/150' };

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
    { source: '/Users/kayahir/Desktop/SWEN732/SWEN732-team1/images/mcimage.jpeg' },
    { source: '/Users/kayahir/Desktop/SWEN732/SWEN732-team1/images/ipimage.png' },
    { source: '/Users/kayahir/Desktop/SWEN732/SWEN732-team1/images/accimage.jpeg' },
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

  const renderItem = ({ item, index }) => {
    return (
      <View style={styles.carouselItem}>
        <Image style={styles.image} source={{ uri: item.source }} />
      </View>
    );
  };

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.navbar}>
        <TextInput
          style={styles.searchInput}
          placeholder="Search..."
          placeholderTextColor="#888"
          value={searchQuery}
          onChangeText={setSearchQuery}
        />
        <Button
          title="Search"
          onPress={() => handleSearch(searchQuery)}
        />
      </View>

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
    paddingHorizontal: 10,
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
