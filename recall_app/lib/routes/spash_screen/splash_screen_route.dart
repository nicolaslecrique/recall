import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../../models/user_model.dart';
import '../home/home_route.dart';

class SplashScreenRoute extends StatefulWidget {
  static const route = '/splash_screen';

  const SplashScreenRoute({Key? key}) : super(key: key);

  @override
  State<SplashScreenRoute> createState() => _SplashScreenRouteState();
}

class _SplashScreenRouteState extends State<SplashScreenRoute> {
  @override
  void initState() {
    super.initState();
    initUser().then((value) => null);
  }

  Future<void> initUser() async {
    var model = Provider.of<UserModel>(context, listen: false);
    // me must get the navigator before first await call
    // cf. https://stackoverflow.com/questions/69466478/waiting-asynchronously-for-navigator-push-linter-warning-appears-use-build
    // and https://dart-lang.github.io/linter/lints/use_build_context_synchronously.html
    var navigator = Navigator.of(context);
    await model.init();
    await navigator.pushNamedAndRemoveUntil(HomeRoute.route, (r) => false);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      //nb: logo is done with https://cooltext.com/
      body: Text("splashscreen"),
    );
  }
}
