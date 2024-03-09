import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';
import { TouchableOpacity } from 'react-native';

const LoginPage = ({ navigation }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [loginMessage, setLoginMessage] = useState('');

  const navigateToSignup = () => {
    navigation.navigate('Signup');
  };
  const handleLogin = () => {
  const url = 'http://127.0.0.1:8081/login';

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
      if (!response.ok) {
        if (response.status === 410) {
          throw new Error('Username or password is wrong');
        } else {
          throw new Error('Some error occurred, please try again later.');
        }
      }
      return response.json();
    })
    .then(data => {
      console.log(data);
      Alert.alert("Login Successfully");
    })
    .catch(error => {
      if (error.message === 'Username or password is wrong') {
        Alert.alert("Invalid Username or Password", error.message);
      } else {
        console.error('Error:', error);
        Alert.alert("Network Error", "Failed to login. Please check your network connection and try again.");
      }
    });
};


return (
    <View style={styles.container}>
      <Text style={styles.title}>Login</Text>
      <TextInput
        style={styles.input}
        placeholder="Username"
      />
      <TextInput
        style={styles.input}
        placeholder="Password"
        secureTextEntry
      />
      <TouchableOpacity style={styles.button} onPress={handleLogin}>
        <Text style={styles.buttonText}>Login</Text>
      </TouchableOpacity>
      <TouchableOpacity onPress={navigateToSignup}>
        <Text style={styles.signupText}>Don't have an account? Sign up</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: 20,
    backgroundColor: '#ffffff',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  input: {
    width: '100%',
    height: 40,
    borderColor: '#cccccc',
    borderWidth: 1,
    borderRadius: 5,
    paddingHorizontal: 10,
    marginBottom: 10,
  },
  button: {
    width: '100%',
    height: 40,
    backgroundColor: '#007bff',
    justifyContent: 'center',
    alignItems: 'center',
    borderRadius: 5,
    marginTop: 10,
  },
  buttonText: {
    color: '#ffffff',
    fontSize: 16,
    fontWeight: 'bold',
  },
  signupText: {
    marginTop: 20,
    color: '#007bff',
    fontSize: 16,
  },
});

export default LoginPage;
