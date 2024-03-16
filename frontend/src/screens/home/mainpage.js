import React from 'react';
import { SafeAreaView, Text, View, ScrollView, TouchableOpacity } from 'react-native';
import tw from 'twrnc';
import { AntDesign } from '@expo/vector-icons';

const MainPage = ({ navigation }) => {
    const handleLogout = () => {
        navigation.navigate('LoginScreen');
      };
  return (
    <SafeAreaView style={tw`flex-1`}>
      <View style={tw`p-4`}>
        <Text style={tw`text-2xl font-bold`}>Welcome back, User!</Text>
        <Text style={tw`text-lg mt-2`}>Ready to crush your fitness goals today?</Text>
      </View>

      <ScrollView style={tw`flex-1`} contentContainerStyle={tw`p-4`}>
        <View style={tw`bg-white p-4 rounded-lg shadow`}>
          <Text style={tw`text-lg font-semibold`}>Your Daily Goals</Text>
          {/* Add your daily goals components here */}
        </View>

        <View style={tw`bg-white p-4 rounded-lg shadow mt-4`}>
          <Text style={tw`text-lg font-semibold`}>Workout Suggestions</Text>
          {/* Add your workout suggestions components here */}
        </View>

        <View style={tw`bg-white p-4 rounded-lg shadow mt-4`}>
          <Text style={tw`text-lg font-semibold`}>Activity Feed</Text>
          {/* Add your activity feed components here */}
        </View>

        <View style={tw`bg-white p-4 rounded-lg shadow mt-4`}>
          <Text style={tw`text-lg font-semibold`}>Challenges</Text>
          {/* Add your challenges components here */}
        </View>

        <View style={tw`bg-white p-4 rounded-lg shadow mt-4`}>
          <Text style={tw`text-lg font-semibold`}>Health Tips</Text>
          {/* Add your health tips components here */}
        </View>
      </ScrollView>

      <View style={tw`p-4 flex-row justify-around`}>
        <TouchableOpacity onPress={() => navigation.navigate('WorkoutPlans')}>
          <AntDesign name="profile" size={24} />
          <Text>Plans</Text>
        </TouchableOpacity>
        <TouchableOpacity onPress={() => navigation.navigate('Nutrition')}>
          <AntDesign name="apple1" size={24} />
          <Text>Nutrition</Text>
        </TouchableOpacity>
        <TouchableOpacity onPress={() => navigation.navigate('Community')}>
          <AntDesign name="team" size={24} />
          <Text>Community</Text>
        </TouchableOpacity>
        <TouchableOpacity onPress={() => navigation.navigate('Settings')}>
          <AntDesign name="setting" size={24} />
          <Text>Settings</Text>
        </TouchableOpacity>
        <TouchableOpacity onPress={handleLogout}>
          <AntDesign name="logout" size={24} />
          <Text>Logout</Text>
        </TouchableOpacity>
      </View>
    </SafeAreaView>
  );
};

export default MainPage;
