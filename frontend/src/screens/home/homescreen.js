import React from 'react';
import { ImageBackground, SafeAreaView, View } from 'react-native';
import tw from 'twrnc';
import StyledButton from '../../components/StyledButton';

const HomePage = ({ navigation }) => {
  return (
    <SafeAreaView style={tw`flex-1 items-center pt-10`}>
      <View style={tw`w-3/4 h-1/2 justify-center items-center mt-20`}>
        <ImageBackground
          source={require('../../assets/images/homepage.png')}
          style={tw`w-full h-full justify-center items-center`}
          resizeMode="contain"
        />
      </View>

      <View style={tw`w-full absolute bottom-20 px-20 flex justify-center items-center`}>
        <StyledButton title="Login" color="gray-800" onPress={() => {navigation.navigate('LoginScreen')}} />
        <StyledButton title="Register" color="gray-800" onPress={() => {navigation.navigate('RegisterScreen')}} />
      </View>
    </SafeAreaView>
  );
};

export default HomePage;
