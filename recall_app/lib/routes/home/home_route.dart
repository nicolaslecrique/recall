import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../../design/constants.dart';
import '../../models/user_model.dart';
import '../login/my_login_screen.dart';

class HomeRoute extends StatefulWidget {
  static const route = '/home';

  const HomeRoute({super.key});

  @override
  State<HomeRoute> createState() => _HomeRouteState();
}

class _HomeRouteState extends State<HomeRoute> {
  @override
  Widget build(BuildContext context) {
    UserModel model = Provider.of<UserModel>(context, listen: false);
    var allItems = model.getAll();
    return Scaffold(
      appBar: AppBar(
        actions: [
          IconButton(
              onPressed: () {
                FirebaseAuth.instance.signOut();
                Navigator.pushReplacementNamed(context, MyLoginScreen.signInRoute);
              },
              icon: const Icon(Icons.account_circle))
        ],
      ),
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(StandardSizes.medium),
          child: Column(
            children: [
              Expanded(
                child: ListView.builder(
                    itemCount: allItems.length,
                    itemBuilder: (context, index) {
                      final item = allItems[index];
                      return ListTile(
                        title: Text(item.title),
                        subtitle: Text(item.content),
                      );
                    }),
              )
            ],
          ),
        ),
      ),
    );
  }
}
