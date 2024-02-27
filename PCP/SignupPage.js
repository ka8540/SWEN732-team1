import React, { useState } from 'react';
import { View, TextInput, Button, Text, StyleSheet, Alert } from 'react-native';

export default function SignupPage({ navigation }) {
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    email: '',
    phoneNumber: '',
    username: '',
    password: '',
    confirmPassword: '',
  });

  const emailRegex = /\S+@\S+\.\S+/; // Simple email validation regex

  const handleSignup = () => {
    if (!emailRegex.test(formData.email)) {
      Alert.alert('Invalid Email', 'Please enter a valid email address.');
      return;
    }
    if (formData.password !== formData.confirmPassword) {
      Alert.alert('Password Mismatch', 'The passwords do not match.');
      return;
    }
    // Implement further signup logic here
    console.log('Signup with:', formData);
    // Navigate to Home Screen or show confirmation
    // navigation.navigate('Login'); // Optionally navigate to login after signup
  };

  const handleChange = (name, value) => {
    setFormData(prevState => ({
      ...prevState,
      [name]: value,
    }));
  };

  return (
    <View style={styles.container}>
      <TextInput
        placeholder="First Name"
        value={formData.firstName}
        onChangeText={value => handleChange('firstName', value)}
        style={styles.input}
      />
      <TextInput
        placeholder="Last Name"
        value={formData.lastName}
        onChangeText={value => handleChange('lastName', value)}
        style={styles.input}
      />
      <TextInput
        placeholder="Email"
        value={formData.email}
        onChangeText={value => handleChange('email', value)}
        keyboardType="email-address"
        style={styles.input}
      />
      <TextInput
        placeholder="Phone Number (Optional)"
        value={formData.phoneNumber}
        onChangeText={value => handleChange('phoneNumber', value)}
        keyboardType="phone-pad"
        style={styles.input}
      />
      <TextInput
        placeholder="Username"
        value={formData.username}
        onChangeText={value => handleChange('username', value)}
        style={styles.input}
      />
      <TextInput
        placeholder="Password"
        value={formData.password}
        onChangeText={value => handleChange('password', value)}
        secureTextEntry
        style={styles.input}
      />
      <TextInput
        placeholder="Confirm Password"
        value={formData.confirmPassword}
        onChangeText={value => handleChange('confirmPassword', value)}
        secureTextEntry
        style={styles.input}
      />
      <Button title="Signup" onPress={handleSignup} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  input: {
    width: '80%',
    padding: 10,
    margin: 10,
    borderWidth: 1,
    borderColor: '#ccc',
  },
});
