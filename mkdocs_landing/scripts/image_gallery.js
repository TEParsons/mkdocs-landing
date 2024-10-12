var scratch
class ImageGalleryElement extends HTMLElement {
    connectedCallback() {
      // assign this to a variable for internal functions to use
      let global_this = this;
      // create preview element
      let preview = document.createElement("div");
      preview.className = "gallery-preview";
      preview.img = document.createElement("img");
      preview.appendChild(preview.img);
      preview.hidden = true;
      // create hide button
      let hide_btn = document.createElement("i");
      hide_btn.className = "gallery-hide-btn";
      hide_btn.classList.add("fa-solid");
      hide_btn.classList.add("fa-eye-slash");
      // add hide button to preview
      preview.appendChild(hide_btn);
      // bind onclick for hide
      hide_btn.onclick = function() {
        // hide preview on click
        preview.img.src = undefined;
        preview.hidden = true;
        // deselect all
        for (let child of global_this.children) {
          child.classList.remove("selected");
        }
      }
      // configure each child
      for (let item of this.children) {
      }
      // insert preview element
      this.insertBefore(preview, this.firstChild);
      // start listening for subsequent children
      let observer = new MutationObserver(this.onChildAdded);
      observer.observe(this, { attributes: false, childList: true, subtree: false });
    }

    onChildAdded () {
        console.log(this)
        // bind onclick to each child
        this.target.onclick = function() {
            // set preview on click
            preview.img.src = this.target.src;
            preview.hidden = false;
            // unmark deselected
            for (let child of this.children) {
                child.classList.remove("selected");
            }
            // mark selected
            this.target.classList.add("selected");
        }
        // set class
        this.target.classList.add("gallery-item");
        // if already selected, do selection
        if (this.target.classList.contains("selected")) {
        this.target.onclick();
        }
    }
  }
  customElements.define("image-gallery", ImageGalleryElement);