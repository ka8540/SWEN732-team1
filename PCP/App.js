import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import LoginPage from './LoginPage'; // Ensure you have this component created
import SignupPage from './SignupPage'; // Ensure you have this component created
import { StyleSheet, Text, View } from 'react-native';

// Create a Stack Navigator
const Stack = createNativeStackNavigator();

// HomeScreen Component (previously the content of App.js)
function HomeScreen() {
  return (
    <View style={styles.container}>
      <Text>Open up App.js to start working on your app!</Text>
      {/* The StatusBar import is removed for simplicity; add it back if needed */}
    </View>
  );
}

// App Component with Navigation
export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Price Compare Plus" component={LoginPage} />
        <Stack.Screen name="Signup" component={SignupPage} />
        <Stack.Screen name="Home" component={HomeScreen} options={{ headerShown: false }} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

// Styles (previously in App.js)
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
