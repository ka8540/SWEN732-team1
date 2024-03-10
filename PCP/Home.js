import React, { useState } from 'react';
import { Ionicons } from '@expo/vector-icons';
import { SafeAreaView, View, Text, StyleSheet, TouchableOpacity, Image, TextInput,Dimensions } from 'react-native';
import Carousel from 'react-native-snap-carousel';

export default function Home() {
  const [searchQuery, setSearchQuery] = useState('');
  const [activeIndex, setActiveIndex] = useState(0);
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
        <Text>Welcome to the Home Screen!</Text>
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
