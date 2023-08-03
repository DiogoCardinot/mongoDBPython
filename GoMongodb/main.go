package main

import (
	"context"
	"fmt"
	"log"
	"time"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
	"go.mongodb.org/mongo-driver/mongo/readpref"
)

func main() {
	client, err := mongo.NewClient(options.Client().ApplyURI("mongodb://localhost:27017")) //conecta o go ao mongodb

	if err != nil {
		log.Fatal(err)
	}
	ctx, _ := context.WithTimeout(context.Background(), 10*time.Second)
	err = client.Connect(ctx)
	if err != nil {
		log.Fatal(err)
	}
	defer client.Disconnect(ctx)
	err = client.Ping(ctx, readpref.Primary())
	if err != nil {
		log.Fatal(err)
	}

	// databases, err := client.ListDatabaseNames(ctx, bson.M{}) //salva as bases de dados do client numa variável
	// if err != nil {
	// 	log.Fatal(err)
	// }
	// fmt.Println(databases)

	testesGoDataBase := client.Database("testesGo")   //entra na base de dados testesGo
	goCollection := testesGoDataBase.Collection("go") //entra na coleção go da base de dados testesGo
	insertOneResult, err := goCollection.InsertOne(ctx, bson.D{
		{"user", "5555"},
		{"produtoDesejado", "4070 Ti"},
		{"precoDesejado", 4500},
	}) //inserir um unico registro
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(insertOneResult.InsertedID)

	// insertManyResults, err := goCollection.InsertMany(ctx, []interface{}{
	// 	bson.D{
	// 		{"user", "5511"},
	// 		{"produtoDesejado", "Tênis Dunk Low"},
	// 		{"precoDesejado", 550},
	// 	},
	// 	bson.D{
	// 		{"user", "5522"},
	// 		{"produtoDesejado", "Dunk Low"},
	// 		{"precoDesejado", 450},
	// 	},
	// }) //inserir vários registros
	// if err != nil {
	// 	log.Fatal(err)
	// }
	// fmt.Println(insertManyResults.InsertedIDs)

	//UPDATE (filtro, atualizacao)
	// updateOne, err := goCollection.UpdateOne(ctx,
	// 	bson.M{"produtoDesejado": "Dunk Low"},
	// 	bson.D{
	// 		{"$set", bson.D{{"produtoDesejado", "4070 Ti"}}},
	// 	},
	// )
	// if err != nil {
	// 	log.Fatal(err)
	// }
	// fmt.Println("Atualizamos %v Registros", updateOne.ModifiedCount)

}
