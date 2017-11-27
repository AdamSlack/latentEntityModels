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
  public selectedEntity : string = 'Select an Entity';
  public selectedBook : string = 'select a book';

  // subscriptions
  private entitySubscription : Subscription;
  private entityTermSubscription : Subscription;
  private bookTitleSubscription : Subscription;

  constructor(public bookQuery : ExplorerApiService) { }

  public requestEntityTerms(entity: string) {
    if(this.entityTermSubscription) {
      this.entityTermSubscription.unsubscribe();
    }
    this.entityTermSubscription = this.bookQuery.requestEntityTerms(this.selectedBook, entity).subscribe((res) => {
      this.selectedEntity = entity;
      this.terms = res.terms;
    })
  }

  public requestEntities(bookTitle: string) {
    this.selectedBook = bookTitle;
    this.entitySubscription = this.bookQuery.requestEntities(bookTitle).subscribe((res) => {
      this.entities = res.entities;
    })
  }

  public request
  
  ngOnInit() {
    this.bookTitleSubscription = this.bookQuery.requestBookTitles().subscribe((res) => {
      this.bookTitles = res.books;
    })
  }

}
