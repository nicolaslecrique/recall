import 'package:firebase_auth/firebase_auth.dart' hide EmailAuthProvider;
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_ui_auth/firebase_ui_auth.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import 'firebase_options.dart';
import 'models/user_model.dart';
import 'routes/home/home_route.dart';
import 'routes/login/my_login_screen.dart';
import 'routes/spash_screen/splash_screen_route.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();

  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );

  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    var emailProvider = [EmailAuthProvider()];

    return MultiProvider(
      providers: [ChangeNotifierProvider(create: (context) => UserModel())],
      child: MaterialApp(
          title: 'Flutter Demo',
          theme: ThemeData(
            primarySwatch: Colors.blue,
          ),
          initialRoute:
              FirebaseAuth.instance.currentUser == null ? MyLoginScreen.registerRoute : SplashScreenRoute.route,
          routes: {
            SplashScreenRoute.route: (BuildContext context) => const SplashScreenRoute(),
            HomeRoute.route: (BuildContext context) => const HomeRoute(),
            MyLoginScreen.registerRoute: (context) {
              return MyLoginScreen(emailProvider: emailProvider, register: true);
            },
            MyLoginScreen.signInRoute: (context) {
              return MyLoginScreen(emailProvider: emailProvider, register: false);
            },
          }),
    );
  }
}
