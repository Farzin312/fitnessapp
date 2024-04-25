import { StatusBar } from 'expo-status-bar';
import { LogBox } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { ThemeProvider } from './src/components/ThemeContext';
import HomePage from './src/screens/home/homescreen';
import LoginScreen from './src/screens/auth/loginscreen';
import MainPage from './src/screens/home/mainpage';
import RegisterScreen from './src/screens/auth/registrationscreen';
import ResetPasswordRequestScreen from './src/screens/auth/resetpasswordrequestscreen';
import Settings from './src/screens/setting/settings';
import Profile from './src/screens/profile/profile';
import Happiness from './src/screens/profile/happiness/happiness';


const Stack = createStackNavigator();
const ThemedStack = createStackNavigator();
LogBox.ignoreLogs(['ViewPropTypes will be removed', 'PropTypes will be removed'])
function ThemedScreens() {
  return (
    <ThemeProvider>
      <ThemedStack.Navigator>
        <ThemedStack.Screen name="MainPage" component={MainPage} options={{ headerShown: false }} />
        <ThemedStack.Screen name="Settings" component={Settings} options={{ headerShown: false }} />
        <ThemedStack.Screen name="Profile" component={Profile} options={{ headerShown: false }} />
        <ThemedStack.Screen name="Happiness" component={Happiness} options={{ headerShown: false }} />
      </ThemedStack.Navigator>
    </ThemeProvider>
  );
}

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="HomePage">
        <Stack.Screen name="HomePage" component={HomePage} options={{ headerShown: false }} />
        <Stack.Screen name="LoginScreen" component={LoginScreen} options={{ headerShown: false }} />
        <Stack.Screen name="RegisterScreen" component={RegisterScreen} options={{ headerShown: false }} />
        <Stack.Screen name="ResetPasswordRequestScreen" component={ResetPasswordRequestScreen} options={{ headerShown: false }} />
        <Stack.Screen name="ThemedScreens" component={ThemedScreens} options={{ headerShown: false }} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
