import React, { useState } from 'react';
import { SafeAreaView, Alert, StyleSheet, Text, View, TextInput, TouchableOpacity, Image,Platform } from 'react-native';
import { StatusBar } from 'expo-status-bar';

export default function App() {
  const [firstname, setFirstName] = useState('');
  const [lastname, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [role,setRole] = useState('');

  const handleSubmit = () => {
    // Endpoint URL
    const url = 'http://127.0.0.1:5000/signUp';
  
    // Form data to be sent
    const formData = {
      firstname: firstname,
      lastname: lastname,
      email: email,
      username: username,
      password: password,
      role: role
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
        <Text style={styles.header}>Sign Up</Text>
        <View style={styles.row}>
        <TextInput
          style={[styles.input, styles.halfInput]}
          placeholder="Firstname"
          value={firstname}
          onChangeText={setFirstName}
        />
        <TextInput
          style={[styles.input, styles.halfInput]}
          placeholder="Lastname"
          value={lastname}
          onChangeText={setLastName}
        />
      </View>
        <TextInput
          style={styles.input}
          placeholder="Email"
          value={email}
          onChangeText={setEmail}
          keyboardType="email-address"
        />

        <TextInput
          style={styles.input}
          placeholder="Username"
          value={username}
          onChangeText={setUsername}
          keyboardType="number-pad"
        />

        <TextInput
          style={styles.input}
          placeholder="Password"
          value={password}
          onChangeText={setPassword}
          keyboardType="number-pad" 
        />

        <TextInput
          style={styles.input}
          placeholder="role"
          value={role}
          onChangeText={setRole}
          keyboardType="number-pad" 
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
    width: '90%',
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
  image: {
    width: 120, 
    height: 100,
    borderRadius: 10,
    marginVertical: 10,
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
