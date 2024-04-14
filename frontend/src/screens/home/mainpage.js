import React, { useState } from 'react';
import { SafeAreaView, Text, View, ScrollView, Modal, Alert } from 'react-native';
import tw from 'twrnc';
import axios from 'axios';
import { useTheme } from '../../components/ThemeContext'; 
import { DarkThemeComponents, LightThemeComponents } from '../../components/ThemeComponents'; 
import { AntDesign } from '@expo/vector-icons';
import StyledButton from '../../components/StyledButton';


const MainPage = ({ navigation, route }) => {
  const { token, userData } = route.params;
  const [newUserName, setNewUserName] = useState('');
  const [isModalVisible, setIsModalVisible] = useState(!userData.profile.name);
  const { isDarkTheme } = useTheme(); 
  const { Section, TextInput, ModalView, TouchOpacity, Background } = isDarkTheme ? DarkThemeComponents : LightThemeComponents;

  const handleSaveUserName = async () => {
    try {
      await axios.patch(`http://127.0.0.1:8000/userprofiles/${userData.profile.id}/`, {
        name: newUserName,
      }, {
        headers: {
          'Authorization': `Token ${token}`,
        },
      });
      setIsModalVisible(false);
      Alert.alert('Success', 'Username saved successfully');
    } catch (error) {
      Alert.alert('Error', 'Failed to save username');
    }
  };


  return (
    <Background style= {tw`w-full h-full z-50`}>
    <SafeAreaView style={tw`flex-1`}>
        <View style={tw`pt-5 justify-center items-center`}>
          <Text style={tw`text-3xl font-bold`}>ActiveTrack</Text>
        </View>
      <View style={tw`w-full h-full z-50`} >
      <ScrollView style={tw`flex-1`} contentContainerStyle={tw`p-4`}>
      <View style={tw`p-4 flex justify-around`}>
        <TouchOpacity onPress={() => navigation.navigate('PersonalInformation')}>
          <AntDesign name="profile" size={24} />
            <Text>Personal Info</Text>
        </TouchOpacity>
        <TouchOpacity onPress={() => navigation.navigate('Diet')}>
          <AntDesign name="appstore-o" size={24}/>
            <Text>Diet</Text>
        </TouchOpacity>
        <TouchOpacity onPress={() => navigation.navigate('Workout')}>
          <AntDesign name="book" size={24} />
            <Text>Workout</Text>
        </TouchOpacity>
        <TouchOpacity onPress={() => navigation.navigate('Rankings')}>
          <AntDesign name="barschart" size={24} />
            <Text>Rankings</Text>
        </TouchOpacity>
        <TouchOpacity onPress={() => navigation.navigate('Settings')}>
          <AntDesign name="setting" size={24} />
            <Text>Settings</Text>
        </TouchOpacity>
      </View>
      </ScrollView>
      <Modal animationType="slide" transparent={true} visible={isModalVisible} onRequestClose={() => setIsModalVisible(false)}>
                <ModalView>
                    <Text style={tw`text-lg font-semibold`}>Set Your Username</Text>
                    <TextInput placeholder="Enter your new username" value={newUserName} onChangeText={setNewUserName} />
                    <StyledButton title="Save Username" onPress={handleSaveUserName} />
                </ModalView>
            </Modal>
      </View>
    </SafeAreaView>
    </Background>
  );
};

export default MainPage;