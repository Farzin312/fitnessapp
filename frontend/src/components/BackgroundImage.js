import React from 'react';
import { Image, StyleSheet } from 'react-native';
import tw from 'twrnc';

const BackgroundImage = ({ style }) => {
  return (
    <Image
      source={require("../assets/images/cloud.png")}
      style={[styles.backgroundImage, style]}
      resizeMode='contain'
    />
  );
};

const styles = StyleSheet.create({
  backgroundImage: tw`absolute bottom-0`,
});

export default BackgroundImage;
