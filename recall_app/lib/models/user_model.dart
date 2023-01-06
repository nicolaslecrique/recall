import 'package:flutter/material.dart';

class UserModel extends ChangeNotifier {
  Future<void> init() async {}

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
