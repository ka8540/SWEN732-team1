import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import Login from './Login';
import SignUp from './Signup'
import Home from './Home'
import Account from './Account';
export default function App() {
  const Stack = createNativeStackNavigator();

  return (
    <NavigationContainer>
    <Stack.Navigator>
      <Stack.Screen name="Login" component={Login} />
      <Stack.Screen name="SignUp" component={SignUp} />
      <Stack.Screen
          name="Home"
          component={Home}
          options={{
            headerLeft: () => null, 
            headerTitleAlign: 'center', 
          }}
        />
      <Stack.Screen    
          name="Account"
          component={Account}
          options={{
            headerLeft: () => null, 
            headerTitleAlign: 'center', 
          }} />  
    </Stack.Navigator>
  </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
