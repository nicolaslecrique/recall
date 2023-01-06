import 'package:firebase_ui_auth/firebase_ui_auth.dart';
import 'package:flutter/material.dart';

import '../spash_screen/splash_screen_route.dart';

class MyLoginScreen extends StatelessWidget {
  static const registerRoute = "/register";
  static const signInRoute = "/sign-in";
  final bool register;

  const MyLoginScreen({Key? key, required this.emailProvider, required this.register}) : super(key: key);

  final List<EmailAuthProvider> emailProvider;

  @override
  Widget build(BuildContext context) {
    var actions = [
      AuthStateChangeAction<SignedIn>(
        (context, state) {
          Navigator.pushReplacementNamed(context, SplashScreenRoute.route);
        },
      ),
      AuthStateChangeAction<UserCreated>(
        (context, state) {
          Navigator.pushReplacementNamed(context, SplashScreenRoute.route);
        },
      ),
    ];

    return register
        ? RegisterScreen(
            providers: emailProvider,
            actions: actions,
          )
        : SignInScreen(
            providers: emailProvider,
            actions: actions,
          );
  }
}
