import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../../models/user_model.dart';

class HomeRoute extends StatefulWidget {
  static const route = '/home';

  const HomeRoute({super.key, required this.title});

  final String title;

  @override
  State<HomeRoute> createState() => _HomeRouteState();
}

class _HomeRouteState extends State<HomeRoute> {
  @override
  Widget build(BuildContext context) {
    UserModel model = Provider.of<UserModel>(context, listen: false);
    return Scaffold(body: Text(model.getAll()[1]));
  }
}
