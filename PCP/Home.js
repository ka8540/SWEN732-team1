import React, { useState } from 'react';
import { Ionicons } from '@expo/vector-icons';
import { SafeAreaView, View, Text, StyleSheet, TouchableOpacity, Image, TextInput } from 'react-native';


export default function Home() {
  const [searchQuery, setSearchQuery] = useState('');

  const handleSearch = (query) => {
    setSearchQuery(query);
    // Perform the search operation here
    // You can call an API or filter local data based on the searchQuery
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
    flexDirection: 'row', // Align items horizontally
    paddingHorizontal: 10, // Add some padding on the sides
  },
  searchInput: {
    flex: 1, // Take up all available space
    height: 40, // Fixed height for the search bar
    backgroundColor: '#fff', // A different background color for the input
    borderRadius: 20, // Rounded corners
    paddingHorizontal: 10, // Inner padding
    fontSize: 16, // Text size
    color: '#000', // Text color
  },
  content: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  footer: {
    flexDirection: 'row', // Change the footer layout to horizontal
    height: 60,
    alignItems: 'center',
    justifyContent: 'space-around', // This will distribute the space around the child components evenly
    backgroundColor: 'cyan',
  },
  footerButton: {
    // Add padding, if needed, to ensure the touchable area is sufficiently large
    paddingHorizontal: 10,
    paddingVertical: 10,
  },
  footerText: {
    fontSize: 16,
    color: '#fff',
  },
  footerIcon: {
    width: 24, // Adjust if necessary
    height: 24, // Adjust if necessary
  },
});
