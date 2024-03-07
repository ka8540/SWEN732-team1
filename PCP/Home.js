import React from 'react';
import { Ionicons } from '@expo/vector-icons';
import { SafeAreaView, View, Text, StyleSheet, TouchableOpacity, Image } from 'react-native';


export default function Home({ navigation }) {
    const handleFooterButtonPress = () => {
        navigation.navigate('Account');
      };  
  return (
    <SafeAreaView style={styles.container}>
      {/* Navbar */}
      <View style={styles.navbar}>
        <Text style={styles.navbarText}>Home Page</Text>
      </View>

      {/* Main Content */}
      <View style={styles.content}>
        <Text>Welcome to the Home Screen!</Text>
      </View>

      {/* Footer */}
      <View style={styles.footer}>
        <TouchableOpacity style={styles.footerButton} onPress={handleFooterButtonPress}>
          {/* Replace 'icon.png' with your actual icon image */}
          <Ionicons name="person-outline" size={32} color="black" />
        </TouchableOpacity>
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
  },
  navbarText: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#fff',
  },
  content: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  footer: {
    height: 60,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: 'cyan',
  },
  footerText: {
    fontSize: 16,
    color: '#fff',
  },
  footerIcon: {
    width: 10, // Adjust the size as needed
    height: 10, // Adjust the size as needed
    marginRight: 12, // Adds some spacing between the icon and the text
  },
  footerButtonText: {
    fontSize: 16,
    color: '#fff',
  }
});
