import { Component, OnInit } from '@angular/core';
import { ExplorerApiService } from '../services/explorer-api.service'
import { Subscription } from 'rxjs/Subscription';
import { Subscriber } from 'rxjs/Subscriber';
@Component({
  selector: 'app-book-explorer',
  templateUrl: './book-explorer.component.html',
  styleUrls: ['./book-explorer.component.scss']
})
export class BookExplorerComponent implements OnInit {


  // variables
  public entities : Array<string>;
  public terms : {term : string, strength : number}
  public bookTitles : Array<string>;
  public topics : Array<{id: string, pct: number}>

  public selectedEntity : string = 'Select an Entity';
  public selectedBook : string = 'select a book';

  // subscriptions
  private entitySubscription : Subscription;
  private entityTermSubscription : Subscription;
  private bookTitleSubscription : Subscription;
  private bookTopicSubscription : Subscription

  constructor(public bookQuery : ExplorerApiService) { }

  public requestEntityTerms(entity: string) {
    if(this.entityTermSubscription) {
      this.entityTermSubscription.unsubscribe();
    }
    this.entityTermSubscription = this.bookQuery.requestEntityTerms(this.selectedBook, entity).subscribe((res) => {
      this.selectedEntity = entity;
      this.terms = res.terms;
    });
  }

  public requestEntities(bookTitle: string) {
    this.selectedBook = bookTitle;
    this.entitySubscription = this.bookQuery.requestEntities(bookTitle).subscribe((res) => {
      this.entities = res.entities;
    })
  }

  public requestTopics(bookTitle: string) {
    if(this.bookTopicSubscription) {
      this.bookTopicSubscription.unsubscribe();
    }
    
    this.bookTopicSubscription = this.bookQuery.requestBookTopics(bookTitle).subscribe((res) => {
      let api_topics = res.topics;
      let sum = api_topics.reduce((a,b) => a + b.score, 0); 
      this.topics = api_topics.map((t) => {
        return {id: 'Topic ' + t.topic_id.toString(), pct: (t.score/sum*100).toFixed(2)}
      }).sort((a,b) => b.pct - a.pct);
    });
  }
  
  

  ngOnInit() {
    this.bookTitleSubscription = this.bookQuery.requestBookTitles().subscribe((res) => {
      this.bookTitles = res.books;
    })
  }

}
