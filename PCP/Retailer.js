import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, TouchableOpacity, FlatList, ActivityIndicator } from 'react-native';
import { useNavigation, useRoute } from '@react-navigation/native';

const Retailer = () => {
  const [retailers, setRetailers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const navigation = useNavigation();
  const route = useRoute();
  const { CategoryId } = route.params; // Get CategoryId from navigation parameters

  useEffect(() => {
    const fetchRetailers = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5000/retailers');
        const data = await response.json();
        setRetailers(data);
      } catch (e) {
        setError('Failed to fetch retailers: ' + e.toString());
      } finally {
        setLoading(false);
      }
    };

    fetchRetailers();
  }, []);

  if (loading) {
    return <View style={styles.centered}><ActivityIndicator size="large" /></View>;
  }

  if (error) {
    return <View style={styles.centered}><Text>{error}</Text></View>;
  }

  const renderItem = ({ item }) => (
    <TouchableOpacity
      style={styles.retailerButton}
      onPress={() => navigation.navigate('Phones', { RetailerID: item.RetailerID, CategoryId: CategoryId })}
    >
      <Text style={styles.retailerButtonText}>{item.RetailerName}</Text>
    </TouchableOpacity>
  );

  return (
    <FlatList
      data={retailers}
      renderItem={renderItem}
      keyExtractor={item => item.RetailerID.toString()}
      contentContainerStyle={styles.container}
    />
  );
};

const styles = StyleSheet.create({
  container: {
    flexGrow: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingVertical: 20,
  },
  centered: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  retailerButton: {
    backgroundColor: '#007bff',
    padding: 15,
    borderRadius: 5,
    marginVertical: 10,
    width: 200,
    alignItems: 'center',
  },
  retailerButtonText: {
    color: 'white',
    fontWeight: 'bold',
    fontSize: 16,
  },
});

export default Retailer;
