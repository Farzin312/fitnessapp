import React from 'react';
import { TouchableOpacity, Text } from 'react-native';
import { AntDesign } from '@expo/vector-icons';
import tw from 'twrnc';

const BackButton = ({ onPress }) => {
    return (
        <TouchableOpacity 
            activeOpacity={0.7} 
            onPress={onPress} 
            style={tw`h-[3rem] w-[3rem] bg-gray-200 rounded-full items-center justify-center`}
        >
            <AntDesign name="arrowleft" size={24} color="black" />
        </TouchableOpacity>
    );
};

export default BackButton;
