import React from 'react';
import { View, StyleSheet } from 'react-native';
import RNPickerSelect from 'react-native-picker-select';
import tw from 'twrnc';

const StyledPicker = ({ onValueChange, items, placeholder }) => {
    return (
        <View style={styles.container}>
            <RNPickerSelect
                onValueChange={onValueChange}
                items={items}
                placeholder={placeholder}
                style={{ inputAndroid: styles.input, inputIOS: styles.input }}
            />
        </View>
    );
};

const styles = StyleSheet.create({
    container: tw`bg-gray-200 p-3 rounded-lg mb-4`,
    input: tw`text-lg`,
});

export default StyledPicker;
