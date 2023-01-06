import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';

import '../login/my_login_screen.dart';

class MyAppBar extends StatelessWidget with PreferredSizeWidget {
  const MyAppBar({
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return AppBar(
      backgroundColor: Colors.white,
      title: TextField(
        decoration: InputDecoration(labelText: "Search", prefixIcon: Icon(Icons.search, color: Colors.black)),
      ),
      actions: [
        IconButton(
            onPressed: () {
              FirebaseAuth.instance.signOut();
              Navigator.pushReplacementNamed(context, MyLoginScreen.signInRoute);
            },
            icon: const Icon(Icons.settings))
      ],
    );
  }

  @override
  Size get preferredSize => const Size.fromHeight(kToolbarHeight);
}
