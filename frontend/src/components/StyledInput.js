import React from 'react';
import { Input } from '@rneui/themed';
import tw from 'twrnc';

const StyledInput = ({ placeholder, keyboardType, secureTextEntry, value, onChangeText }) => {
  return (
    <Input
      containerStyle={tw`w-full my-4`}
      inputContainerStyle={tw`py-2`}
      placeholder={placeholder}
      keyboardType={keyboardType}
      secureTextEntry={secureTextEntry}
      value={value}
      onChangeText={onChangeText}
    />
  );
};

export default StyledInput;
