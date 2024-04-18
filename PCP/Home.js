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
    let imageSource = { uri: 'https://via.placeholder.com/150' }; 
    
    if (item.CategoryName === 'TV & Video') {
      imageSource = { uri: 'https://www.digitaltrends.com/wp-content/uploads/2022/12/Sony-75-inch-X95J-Series-4K-TV.jpg' };
    } else if (item.CategoryName === 'Home Audio & Theater') {
      imageSource = { uri: 'https://www.bhphotovideo.com/cdn-cgi/image/format=auto,fit=scale-down,width=500,quality=95/https://www.bhphotovideo.com/images/images500x500/enclave_audio_technologies_ea_1000_pro_thx_cinehome_pro_edition_5_1_1585224397_1554695.jpg' };
    } else if (item.CategoryName === 'Camera Photo & Video') {
      imageSource = { uri: 'data:image/jpeg;base64,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' };
    } else if (item.CategoryName === 'Cell Phones & Accessories') {
      imageSource = { uri: 'https://media.wired.com/photos/5b22c5c4b878a15e9ce80d92/master/w_2240,c_limit/iphonex-TA.jpg' };
    } else if (item.CategoryName === 'Headphones') {
      imageSource = { uri: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0j9eu-xoKRtWZAk701ireSFxve150zD6Swg&s' };
    } else if (item.CategoryName === 'Video Games') {
      imageSource = { uri: 'https://a0.anyrgb.com/pngimg/596/620/analog-stick-gamepad-joystick-game-controller-game-controllers-controller-computer-hardware-video-game-electronics-monochrome-thumbnail.png' };
    } else if (item.CategoryName === 'Bluetooth & Wireless Speakers') {
      imageSource = { uri: 'https://i.ebayimg.com/images/g/xIcAAOSwQBpiA3y1/s-l1200.webp' };
    } else if (item.CategoryName === 'Car Electronics') {
      imageSource = { uri: 'https://www.shutterstock.com/image-vector/electric-car-e-plug-green-600nw-2303576823.jpg' };
    } else if (item.CategoryName === 'Musical Instruments') {
      imageSource = { uri: 'https://upload.wikimedia.org/wikipedia/commons/4/45/GuitareClassique5.png' };
    } else if (item.CategoryName === 'Wearable Technology') {
      imageSource = { uri: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvc6dYdSWzTOK05bo18hZx3Ix3FYRQFx_WNg&s' };
    } else if (item.CategoryName === 'Laptops') {
      imageSource = { uri: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJVAu2vLXne-HWnDzE4ntJ-YlHLQAa6x0m1A&s' };
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