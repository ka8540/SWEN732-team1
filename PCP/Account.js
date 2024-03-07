import React from 'react';
import { SafeAreaView, View, Text, StyleSheet, TouchableOpacity, Alert } from 'react-native';
import { MaterialCommunityIcons } from '@expo/vector-icons';

export default function Account({ navigation }) {
    const handleLogout = () => {
        // Show confirmation dialog
        Alert.alert(
            "Logout", // Title
            "Are you sure you want to logout?", // Message
            [
                {
                    text: "Cancel",
                    onPress: () => console.log("Cancel Pressed"),
                    style: "cancel"
                },
                { 
                    text: "Yes", onPress: () => {
                      console.log("Logout Pressed");
                      // Reset the navigation stack to the Login route
                      navigation.reset({
                        index: 0,
                        routes: [{ name: 'Login' }],
                      });
                    } 
                  }
            ]
        );
    };

  return (
    <SafeAreaView style={styles.container}>
      {/* Navbar */}
      <View style={styles.navbar}>
        <Text style={styles.navbarText}>Account</Text>
      </View>

      {/* Main Content */}
      <View style={styles.content}>
        <MaterialCommunityIcons name="account-circle" size={100} color="black" />
        <Text style={styles.username}>Username</Text>
        {/* Additional account information can be placed here */}
      </View>

      {/* Logout Button */}
      <TouchableOpacity style={styles.button} onPress={handleLogout}>
        <Text style={styles.buttonText}>Logout</Text>
      </TouchableOpacity>
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
    marginBottom: 60, // Leave space for the logout button
  },
  username: {
    fontSize: 24,
    marginVertical: 20,
  },
  button: {
    height: 60,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: 'navy',
  },
  buttonText: {
    fontSize: 20,
    color: '#fff',
    fontWeight: 'bold',
  },
});
