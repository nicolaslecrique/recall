import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';

import '../firebase_options.dart';

class UserModel extends ChangeNotifier {
  Future<void> init() async {
    await Firebase.initializeApp(
      options: DefaultFirebaseOptions.currentPlatform,
    );
  }

  List<String> getAll() {
    return List.of(["aa", "bb", "cc"]);
  }
}
