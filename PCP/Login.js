import React, { useState } from 'react';
import { SafeAreaView, Alert, StyleSheet, Text, View, TextInput, TouchableOpacity,Image} from 'react-native';
import { Platform,StatusBar } from 'expo-status-bar';

export default function Login({ navigation }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const navigateToSignUp = () => {
    navigation.navigate('SignUp');
  };
  const handleSubmit = () => {
    const url = 'http://127.0.0.1:5000/login';
  
    const formData = {
      username: username,
      password: password,
    };
  
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData),
    };
  
    fetch(url, requestOptions)
    .then(response => {
      if (response.ok) {
        return response.json();
      } else if (response.status === 410) {
        throw new Error('username or password is wrong');
      }  else if (response.status === 411) {
        throw new Error('Invalid Password');
      } else {
        throw new Error('Some error occurred, please try again later.');
      }
    })
    .then(data => {
      console.log(data);
      Alert.alert("Login Successfully");
    })
    .catch(error => {
      if (error.message === 'username or password is wrong') {
        Alert.alert("Invalide Username or Password", error.message);
      }else if (error.message === 'Invalid Password') {
        Alert.alert("Password is incorrect", error.message);
      }else {
        console.error('Error:', error);
      }
    });
  };
  

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar style="auto" />
      
      {/* Orange Navbar */}
      <TouchableOpacity onPress={navigateToSignUp} style={styles.signupButton}>
        <Text style={styles.signupButtonText}>Signup</Text>
      </TouchableOpacity>
      
      {/* App Content */}
      <View style={styles.content}>
      <Image 
          source={{ uri: '/Users/kayahir/Desktop/SWEN732/SWEN732-team1/images/icon.png' }} 
          style={styles.image}
        />
        <Text style={styles.header}>Login</Text>
        <View style={styles.row}>
      </View>

      <TextInput
        style={styles.input}
        placeholder="Username"
        value={username}
        onChangeText={setUsername}
        keyboardType="default"
        />
      <TextInput
        style={styles.input}
        placeholder="Password"
        value={password}
        onChangeText={setPassword}
        keyboardType="default"
        secureTextEntry={true}
        />

        <TouchableOpacity onPress={handleSubmit} style={styles.button}>
          <Text style={styles.buttonText}>Login</Text>
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
    backgroundColor: 'orange',
    alignItems: 'center',
    justifyContent: 'flex-start',
    flexDirection: 'row',
    paddingHorizontal: 10,
  },
  navbarText: {
    color: '#fff',
    fontSize: 18,
    fontWeight: 'bold',
  },
  signupButton: {
    backgroundColor: 'green', 
    padding: 5,
    marginTop: 5,
    marginLeft:300, // Adjust the margin as needed
    borderRadius: 10,
    width: '20%',
    alignItems: 'center',
  },
  signupButtonText: {
    color: 'white',
    fontWeight: 'bold',
  },
  content: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    padding: 20,
  },
  header: {
    fontSize: 24,
    fontWeight: 'bold',
    margin: 10,
  },
  input: {
    height: 50,
    marginVertical: 10,
    borderWidth: 1,
    padding: 15,
    width: 200,
    borderRadius: 10,
    backgroundColor: '#fff',
  },
  image: {
    width: 120, 
    height: 250,
    borderRadius: 5,
  },
  button: {
    backgroundColor: 'navy',
    padding: 15,
    marginTop: 20,
    borderRadius: 10,
    width: '70%',
    alignItems: 'center',
  },
  buttonText: {
    color: 'white',
    fontWeight: 'bold',
  },
  row: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    width: '90%',
  },
  halfInput: {
    width: '48%', 
  }
  
});