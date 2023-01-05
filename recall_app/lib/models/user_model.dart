import 'package:flutter/material.dart';

class UserModel extends ChangeNotifier {
  Future<void> init() async {}

  List<String> getAll() {
    return List.of(["aa", "bb", "cc"]);
  }
}
