import React from 'react';
import { SafeAreaView, View, Text, StyleSheet } from 'react-native';

export default function Home() {
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
        <Text style={styles.footerText}>Footer Content Here</Text>
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
});
