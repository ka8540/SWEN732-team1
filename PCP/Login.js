import React, { useState } from 'react';
import { SafeAreaView, Alert, StyleSheet, Text, View, TextInput, TouchableOpacity} from 'react-native';
import { StatusBar } from 'expo-status-bar';

export default function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = () => {
    // Endpoint URL
    const url = 'http://127.0.0.1:5000/login';
  
    // Form data to be sent
    const formData = {
      username: username,
      password: password,
    };
  
    // POST request options
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData),
    };
  
    fetch(url, requestOptions)
    .then(response => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error('Network response was not ok.');
      }
    })
    .then(data => {
      console.log(data);
      Alert.alert("Success", "Form submitted successfully.");
    })
    .catch(error => {
      console.error('There was an error!', error);
      Alert.alert("Network Error", "Failed to submit form. Please check your network connection and try again.");
    });

  };

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar style="auto" />
      
      {/* Orange Navbar */}
      <View style={styles.navbar}>
      </View>
      
      {/* App Content */}
      <View style={styles.content}>
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
          <Text style={styles.buttonText}>Submit</Text>
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
  button: {
    backgroundColor: 'navy',
    padding: 15,
    marginTop: 20,
    borderRadius: 10,
    width: '90%',
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