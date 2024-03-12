import React from 'react';
import { Button } from '@rneui/themed';
import tw from 'twrnc';

const StyledButton = ({ title, onPress }) => {
  return (
    <Button
      title={title}
      onPress={onPress}
      buttonStyle={tw`rounded-100 py-3 w-[15rem] mt-4 bg-black text-white`}
    />
  );
};

export default StyledButton;
