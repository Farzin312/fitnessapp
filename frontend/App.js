import { StatusBar } from 'expo-status-bar';
import { View } from 'react-native';
import tw from 'twrnc';
import LoginScreen from './src/screens/auth/LoginScreen';

export default function App() {
  return (
    <View style={tw`flex-1`}>
      <StatusBar style="auto" />
      <LoginScreen />
    </View>
  );
}
