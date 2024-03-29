import React, { useState, useEffect } from 'react';
import { SafeAreaView, Text, View, ScrollView, TouchableOpacity, Modal, Alert } from 'react-native';
import tw from 'twrnc';
import axios from 'axios';
import { AntDesign } from '@expo/vector-icons';
import StyledButton from '../../components/StyledButton';
import StyledInput from '../../components/StyledInput';

const MainPage = ({ navigation, route }) => {
  const { token } = route.params;
  const [userName, setUserName] = useState('');
  const [newUserName, setNewUserName] = useState('');
  const [isModalVisible, setIsModalVisible] = useState(false);

  const handleLogout = () => {
    navigation.navigate('LoginScreen');
  };

  const fetchUserName = async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/api/userprofiles/${profileId}/`, {
        headers: {
          'Authorization': `Token ${token}`,
        },
      });
      setUserName(response.data.name);
      if (!response.data.name) {
        setIsModalVisible(true);
      }
    } catch (error) {
      console.log(error.response.data);
    }
  };

  const handleSaveUserName = async () => {
    try {
      await axios.patch(`http://127.0.0.1:8000/api/userprofiles/${profileId}/`, {
        name: newUserName,
      }, {
        headers: {
          'Authorization': `Token ${token}`,
        },
      });
      setUserName(newUserName);
      setIsModalVisible(false);
    } catch (error) {
      Alert.alert('Error', 'Failed to save username');
      console.log(error);
    }
  };

  useEffect(() => {
    fetchUserName();
  }, []);

  return (
    <SafeAreaView style={tw`flex-1`}>
      <View style={tw`p-4`}>
        <Text style={tw`text-2xl font-bold`}>Welcome back, {userName || 'User'}!</Text>
      </View>

      <ScrollView style={tw`flex-1`} contentContainerStyle={tw`p-4`}>
        <View style={tw`bg-white p-4 rounded-lg shadow`}>
          <Text style={tw`text-lg font-semibold`}>Personal Information</Text>
          <Text style={tw`text-sm`}>Height, Weight, BMI, etc.</Text>
        </View>

        <View style={tw`bg-white p-4 rounded-lg shadow mt-4`}>
          <Text style={tw`text-lg font-semibold`}>Diet</Text>
          <Text style={tw`text-sm`}>Calorie intake, macronutrient breakdown, etc.</Text>
        </View>

        <View style={tw`bg-white p-4 rounded-lg shadow mt-4`}>
          <Text style={tw`text-lg font-semibold`}>Workout</Text>
          <Text style={tw`text-sm`}>History, progress, goals, etc.</Text>
        </View>

        <View style={tw`bg-white p-4 rounded-lg shadow mt-4`}>
          <Text style={tw`text-lg font-semibold`}>Rankings</Text>
          <Text style={tw`text-sm`}>Overall, by category, etc.</Text>
        </View>
      </ScrollView>

      <View style={tw`p-4 flex-row justify-around`}>
        <TouchableOpacity onPress={() => navigation.navigate('PersonalInformation')}>
          <AntDesign name="profile" size={24} />
          <Text>Personal Info</Text>
        </TouchableOpacity>
        <TouchableOpacity onPress={() => navigation.navigate('Diet')}>
          <AntDesign name="appstore-o" size={24} />
          <Text>Diet</Text>
        </TouchableOpacity>
        <TouchableOpacity onPress={() => navigation.navigate('Workout')}>
          <AntDesign name="book" size={24} />
          <Text>Workout</Text>
        </TouchableOpacity>
        <TouchableOpacity onPress={() => navigation.navigate('Rankings')}>
          <AntDesign name="barschart" size={24} />
          <Text>Rankings</Text>
        </TouchableOpacity>
        <TouchableOpacity onPress={handleLogout}>
          <AntDesign name="logout" size={24} />
          <Text>Logout</Text>
        </TouchableOpacity>
      </View>

      <Modal
        animationType="slide"
        transparent={true}
        visible={isModalVisible}
        onRequestClose={() => setIsModalVisible(false)}
      >
        <View style={tw`flex-1 justify-center items-center bg-gray-900 bg-opacity-50`}>
          <View style={tw`bg-white p-4 rounded-lg shadow`}>
            <Text style={tw`text-lg font-semibold`}>Set Your Username</Text>
            <StyledInput
              placeholder="Enter your new username"
              value={newUserName}
              onChangeText={setNewUserName}
            />
            <View style={tw`w-full items-center mt-4`}>
              <StyledButton title="Save Username" onPress={handleSaveUserName} />
            </View>
          </View>
        </View>
      </Modal>
    </SafeAreaView>
  );
};

export default MainPage;