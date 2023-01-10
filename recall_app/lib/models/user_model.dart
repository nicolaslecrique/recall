import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:recall_app/models/server_api.dart';

import 'server.dart';

class UserModel extends ChangeNotifier {
  late User authUser;

  // it's called after the currentUser is defined (either at startup of
  // after login screen)
  Future<void> init() async {
    authUser = FirebaseAuth.instance.currentUser!;
    var jwtToken = await authUser.getIdToken();
    ServerUser user = await Server.getUser(jwtToken);
  }

  List<Item> getAll() {
    return List.of([
      Item("title 1", "blab bla bla bla"),
      Item("title 2", "blab bla bla bla"),
      Item("title 3", "blab bla bla bla"),
      Item("title 4", "blab bla bla bla"),
      Item("title 5", "blab bla bla bla"),
      Item("title 6", "blab bla bla bla"),
    ]);
  }
}

class Item {
  final String title;
  final String content;

  const Item(this.title, this.content);
}
