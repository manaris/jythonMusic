import jm.audio.io.*;
import jm.audio.synth.*;
import jm.music.data.Note;
import jm.audio.AudioObject;
import jm.audio.AOException;


/**
 * A basic additive synthesis jMusic instrument implementation
 * which implements envelope and volume control
 * @author Andrew Sorensen
 */

public final class SinewavePatch extends jm.audio.Instrument
{
	//----------------------------------------------
	// Attributes
	//----------------------------------------------
	
	/** The number of channels */
	private int channels = 2;
	/** the sample rate passed to the instrument */
	private int sampleRate = 44100;
	/** The pitch in hertz of a fixed frequency oscillator */
	private float frequency = 440.0f;
	/** The break point values for the amplitude envelope (1D list of float pairs - time percent index in generated note (0.0 to 1.0) and amplitude (0.0 to 1.0) at corresponding time index */
	private double[] envelopePoints = {0.0, 0.0, 
                                       0.15, 1.0, 
                                       0.3, 0.5, 
                                       1.0, 0.0};

    // *** (BZM) this.volume is removed, since it apparently overrides a super.volume variable,
    //           which instroduces side-effects.  Thus, no this.getVolume() method.                                   
	/** The volume of the instrument (0.0 to 1.0) */
	//private double volume = 0.0;
	
	/** The panoramic of the instrument (0.0, left to 1.0, right) */
	private double panoramic = 0.5;

    /** Sound components */
    private Oscillator oscillatorBox;
	private Envelope envelopeBox;
	private	Volume volumeBox;
	private	StereoPan panoramicBox;
    private SampleOut soutBox;

	//----------------------------------------------
	// Constructor
	//----------------------------------------------
	/**
	 * Basic default constructor that creates 
	 * a stereo signal at 44100 hz.
	 */
	public SinewavePatch()
	{
	    //this(this.sampleRate, this.channels, this.envelopePoints, this.frequency);
	}
    
    /**
	 * Basic default constructor to set an initial 
	 * sampling rate.
	 * @param sampleRate 
	 */
	public SinewavePatch(int sampleRate)
	{
		this.sampleRate = sampleRate;
	    //this(sampleRate, this.channels, this.envelopePoints, this.frequency);
	}
    
	/**
	 * A constructor to set an initial 
	 * sampling rate and number of channels.
	 * @param sampleRate
     * @param channels the number of channels in the sound 1 = mono, 2 = stereo, etc
	 */
	public SinewavePatch(int sampleRate, int channels)
	{
		this.sampleRate = sampleRate;
		this.channels = channels;
		//this(sampleRate, channels, this.envelopePoints, this.frequency);
	}
    
	/**
	* A constructor to set sampleRate, channels, and 
	* the pitch of the sine wave in hertz.
	* @param sampleRate
	* @param channels the number of channels in the sound 1 = mono, 2 = stereo, etc
	* @param envelopePoints The break point values for the amplitude envelope
	*/
	public SinewavePatch(int sampleRate, int channels, double[] envelopePoints)
	{
		this.sampleRate = sampleRate;
		this.channels = channels;
		this.envelopePoints = envelopePoints;
		//this(sampleRate, channels, envelopePoints, this.frequency);
	}

	/**
	* A constructor to set sampleRate, channels, and 
	* the pitch of the sine wave in hertz.
	* @param sampleRate
	* @param channels the number of channels in the sound 1 = mono, 2 = stereo, etc
	* @param envelopePoints The break point values for the amplitude envelope
	* @param frequency a positive float value specifying a fixed pitch
	*/
	public SinewavePatch(int sampleRate, int channels, double[] envelopePoints, float frequency)
	{
		this.sampleRate = sampleRate;
		this.channels = channels;
		this.envelopePoints = envelopePoints;
		this.frequency = frequency;               
	}
                
	//----------------------------------------------
	// Methods 
	//----------------------------------------------
	/**
	 * Initialisation method used to build the objects that
	 * this instrument will use.
	 */
	public void createChain() throws AOException
	{
		this.oscillatorBox = new Oscillator(this, Oscillator.SINE_WAVE, this.sampleRate, this.channels);
		// set a fixed, rather the note determined, frequency
		if (frequency != -1.0f) { 
			this.oscillatorBox.setChoice(0);
			this.oscillatorBox.setFrq(frequency);
		}

		this.envelopeBox = new Envelope( this.oscillatorBox, this.envelopePoints );
		this.volumeBox = new Volume( this.envelopeBox );
		this.panoramicBox = new StereoPan( this.volumeBox );

        // decide if to generate live sound, or to write in an audio file
		if (output == RENDER) 
		   this.soutBox = new SampleOut( this.panoramicBox );
	}	

	/**
	* Set the frequency of the oscillator.
	* @param frequency - The frequency in hertz
	*/
	public void setFrequency(float frequency) 
	{
	    this.frequency = frequency;
		this.oscillatorBox.setFrq( this.frequency );
	}
        
	/**
	* Get the frequency of the oscillator.
	*/
	public float getFrequency() 
	{
	    return this.frequency;
	}
        
    /**
    * Set the sound envelope.
    * @param envelopePoints - The array of time percent, amplitude pairs of double values.
    */
    public void setEnvelopePoints(double[] envelopePoints) 
    {
        this.envelopePoints = envelopePoints;
        this.envelopeBox.setBreakPoints(envelopePoints);
    }
	
    /**
    * Get the sound envelope.
    */
    public double[] getEnvelopePoints() 
    {
        return this.envelopePoints;
    }
	
    /**
    * Set the sound volume.
    * @param volume - The new volume (0.0 to 1.0).
    */
    public void setVolume(double volume) 
    {
        //this.volume = volume;
        this.volumeBox.setVolume(volume);
    }
	
	
    /**
    * Get the sound volume.
    */
//    public double getVolume() 
//    {
//        return this.volume;
//    }
	
    /**
    * Set the stereo panoramic.
    * @param panoramic - The new panoramic (0.0 to 1.0).
    */
    public void setPanoramic(double panoramic) 
    {
        this.panoramic = panoramic;
        this.panoramicBox.setPan( this.panoramic );
    }

    /**
    * Get the stereo panoramic.
    */
    public double getPanoramic() 
    {
        return this.panoramic;
    }
	
}

